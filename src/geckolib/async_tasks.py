"""AsyncTasks is a class to farm intenal new tasks out to an awaiter."""

import asyncio
import logging
from collections.abc import Coroutine
from typing import Self

from .config import GeckoConfig, config_sleep, release_config_change_waiters

_LOGGER = logging.getLogger(__name__)


class AsyncTasks:
    """
    Manage async tasks.

    Allow clients to have tasks in batches so that they can be controlled
    individually, or cancelled in a block.

    Can be used in a 'with AsyncTasks' pattern which will run the tasks
    in the event loop.
    """

    def __init__(self) -> None:
        """Initialize async tasks class."""
        self._tasks: list[asyncio.Task] = []

    async def __aenter__(self) -> Self:
        """Async enter, used from python's with statement."""
        _LOGGER.debug("Async start, adding tidy routine")
        self.add_task(self._tidy(), "Tidy tasks", "ASYNC")
        return self

    async def __aexit__(self, *_exc_info: object) -> None:
        """Async exit, when out of scope."""
        await self.gather()

    def add_task(self, coroutine: Coroutine, name_: str, key_: str) -> asyncio.Task:
        """Add tasks to the task list."""
        taskname = f"{key_}:{name_}"
        for task in self._tasks:
            if not task.done() and task.get_name() == taskname:
                msg = f"Task {taskname} already running"
                raise RuntimeError(msg)
        _LOGGER.debug("Starting task `%s` in domain `%s`", name_, key_)
        task = asyncio.create_task(coroutine, name=taskname)
        self._tasks.append(task)
        return task

    def cancel_key_tasks(self, key_: str) -> None:
        """Cancel tasks that use the specified key."""
        for task in self._tasks:
            if task.get_name().startswith(f"{key_}:"):
                _LOGGER.debug("Cancel task %s", task)
                task.cancel()
        release_config_change_waiters()

    async def gather(self) -> None:
        """Cancel all tasks."""
        for task in self._tasks:
            _LOGGER.debug("Cancel task %s", task)
            task.cancel()
        # Wait for all tasks to complete
        try:
            _results = await asyncio.gather(*self._tasks, return_exceptions=True)
            for item in zip(self._tasks, _results, strict=False):
                _LOGGER.debug("    Task %s result `%r`", item[0].get_name(), item[1])
        except Exception:
            _LOGGER.exception("AsyncTasks:gather caught exception")
            raise

    async def _tidy(self) -> None:
        try:
            while True:
                await config_sleep(
                    GeckoConfig.TASK_TIDY_FREQUENCY_IN_SECONDS, "Async task tidy"
                )
                create_new_tasks = False
                if _LOGGER.isEnabledFor(logging.DEBUG):
                    for task in self._tasks:
                        if task.done():
                            _LOGGER.debug("Tidy task %s", task)
                            create_new_tasks = True
                # Create a new task list with the currently running ones
                if create_new_tasks:
                    self._tasks = [task for task in self._tasks if not task.done()]
        except asyncio.CancelledError:
            _LOGGER.debug("Tidy loop cancelled")
            raise
        except Exception:
            _LOGGER.exception("Tidy loop caught exception")
            raise
