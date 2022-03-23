"""AsyncTasks is a class to farm intenal new tasks out to an awaiter"""

import logging
import asyncio
from .config import GeckoConfig, config_sleep

_LOGGER = logging.getLogger(__name__)


class AsyncTasks:
    def __init__(self):
        self._tasks = []

    async def __aenter__(self):
        self.add_task(self._tidy(), "Tidy tasks", "ASYNC")

    async def __aexit__(self, *exc_info) -> None:
        await self.gather()

    def add_task(self, coroutine, name_: str, key_: str) -> None:
        _LOGGER.debug("Starting task `%s` in domain `%s`", name_, key_)
        task = asyncio.create_task(coroutine, name=f"{key_}:{name_}")
        self._tasks.append(task)

    def cancel_key_tasks(self, key_: str) -> None:
        for task in self._tasks:
            if task.get_name().startswith(f"{key_}:"):
                _LOGGER.debug("Cancel task %s", task)
                task.cancel()

    async def gather(self) -> None:
        # Cancel all tasks
        for task in self._tasks:
            _LOGGER.debug("Cancel task %s", task)
            task.cancel()
        # Wait for all tasks to complete
        _results = await asyncio.gather(*self._tasks, return_exceptions=True)
        for item in zip(self._tasks, _results):
            _LOGGER.debug("    Task %s result `%r`", item[0].get_name(), item[1])

    async def _tidy(self) -> None:
        try:
            while True:
                await config_sleep(GeckoConfig.TASK_TIDY_FREQUENCY_IN_SECONDS)
                if _LOGGER.isEnabledFor(logging.DEBUG):
                    for task in self._tasks:
                        if task.done():
                            _LOGGER.debug("Tidy task %s", task)
                self._tasks = [task for task in self._tasks if not task.done()]
        except asyncio.CancelledError:
            _LOGGER.debug("Tidy loop cancelled")
            raise

    @property
    def unique_id(self) -> str:
        """Dummy function designed to be overridden."""
        # TODO: Find a better way, this isn't functionality that the task manager needs
        return ""

    @property
    def spa_name(self) -> str:
        """Dummy function designed to be overridden"""
        # TODO: Find a better way, this isn't functionality that the task manager needs
        return ""
