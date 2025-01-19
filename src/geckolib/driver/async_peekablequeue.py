"""A peekable async queue"""

import asyncio.queues
from typing import Any


class AsyncPeekableQueue(asyncio.queues.Queue):
    """A peekable async queue which allows queue filtering in consumers."""

    def __init__(self):
        """Initialize the async peekable queue."""
        super().__init__()
        self._marked = False

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
        self.get_nowait()
        self.task_done()
        self._marked = False

    def mark(self) -> None:
        """Mark the queue."""
        self._marked = True
