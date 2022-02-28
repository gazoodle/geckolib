"""AsyncTasks is a class to farm intenal new tasks out to an awaiter"""

from asyncio import tasks
import logging
import asyncio

_LOGGER = logging.getLogger(__name__)


class AsyncTasks:
    def __init__(self):
        self._tasks = []
        self.add_task(self._tidy(), "Tidy tasks")

    async def __aexit__(self, *exc_info):
        await self.gather()

    def add_task(self, coroutine, name_):
        self._tasks.append(asyncio.create_task(coroutine, name=name_))

    async def gather(self):
        # Cancel all tasks
        for task in self._tasks:
            _LOGGER.debug("Cancel task %s", task)
            task.cancel()
        # Wait for all tasks to complete
        task_results = await asyncio.gather(*self._tasks, return_exceptions=True)
        _LOGGER.debug("Async tasks: results %s", task_results)

    async def _tidy(self):
        while True:
            # Run every five seconds
            await asyncio.sleep(5)
            self._tasks = [task for task in self._tasks if not task.done()]
