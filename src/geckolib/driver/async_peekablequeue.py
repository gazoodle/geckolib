"""A peekable async queue."""

import asyncio.queues
import collections
from asyncio import QueueShutDown
from typing import Any


class AsyncPeekableQueue(asyncio.queues.Queue):
    """A peekable async queue which allows queue filtering in consumers."""

    def __init__(self):
        """Initialize the async peekable queue."""
        super().__init__()
        self._marked = False
        self._data_available = asyncio.Event()

    def _init(self, maxsize) -> None:
        self._queue = collections.deque()

    def _get(self) -> Any:
        item = self._queue.popleft()
        if self.empty():
            self._data_available.clear()
        return item

    def _put(self, item: Any) -> None:
        self._queue.append(item)
        self._data_available.set()

    @property
    def head(self) -> Any:
        """Get the queue head or None."""
        if self.qsize() > 0:
            return self._queue[0]
        return None

    @property
    def is_marked(self) -> bool:
        """Get the is_marked property."""
        return self._marked

    def pop(self) -> Any:
        """Pop the item off the top of the queue."""
        item = self.get_nowait()
        self.task_done()
        self._marked = False
        return item

    def mark(self) -> None:
        """Mark the queue."""
        self._marked = True

    async def wait(self) -> None:
        """Wait for there to be data queued."""
        await self._data_available.wait()
