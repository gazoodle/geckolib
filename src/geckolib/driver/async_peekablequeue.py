"""A peekable async queue."""

import asyncio.queues
import collections
from typing import Any


class AsyncPeekableQueue:
    """A peekable async queue which allows queue filtering in consumers."""

    def __init__(self) -> None:
        """Initialize the async peekable queue."""
        self._marked = False
        self._normal_queue = collections.deque()
        self._command_queue = collections.deque()
        self._data_available = asyncio.Event()

    def _set_state(self) -> None:
        if self._command_queue or self._normal_queue:
            self._data_available.set()
        else:
            self._data_available.clear()

    def peek(self) -> Any:
        """Get the queue head or None."""
        if self._command_queue:
            return self._command_queue[0]
        if self._normal_queue:
            return self._normal_queue[0]
        return None

    @property
    def is_data_available(self) -> bool:
        """Is there any data available."""
        return self._data_available.is_set()

    @property
    def is_marked(self) -> bool:
        """Get the is_marked property."""
        return self._marked

    def pop(self) -> Any:
        """Pop the item off the top of the queue."""
        try:
            if self._command_queue:
                return self._command_queue.popleft()
            return self._normal_queue.popleft()
        finally:
            self._set_state()
            self._marked = False

    def push(self, item: Any) -> None:
        """Push an item on the bottom of the queue."""
        self._normal_queue.append(item)
        self._set_state()
        self._marked = False

    def push_command(self, item: Any) -> None:
        """Push an item on the bottom of the command queue."""
        self._command_queue.append(item)
        self._set_state()
        self._marked = False

    def mark(self) -> None:
        """Mark the queue."""
        self._marked = True

    async def wait(self) -> None:
        """Wait for there to be data queued."""
        await self._data_available.wait()

    def __bool__(self) -> bool:
        """Determine if there are any items in the queue."""
        return len(self) > 0

    def __len__(self) -> int:
        """Implement the __len__ function."""
        return self._command_queue.__len__() + self._normal_queue.__len__()
