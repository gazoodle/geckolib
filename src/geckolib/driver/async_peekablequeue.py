"""A peekable async queue"""

import asyncio.queues

class AsyncPeekableQueue(asyncio.queues.Queue):
    """A peekable async queue which allows queue filtering in consumers"""

    def __init__(self):
        super().__init__()
        self._marked = False

    @property
    def head(self):
        """The head property will reveal the item at the head of the queue
        if there is one, or None if there isn't one"""
        if self.qsize() > 0:
            return self._queue[0]
        return None

    @property
    def is_marked(self):
        return self._marked

    def pop(self):
        self.get_nowait()
        self._marked = False

    def mark(self):
        self._marked = True
