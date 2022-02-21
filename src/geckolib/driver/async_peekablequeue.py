"""A peekable async queue"""

import asyncio.queues

class AsyncPeekableQueue(asyncio.queues.Queue):
    """A peekable async queue which allows queue filtering in consumers"""

    @property
    def head(self):
        """The head property will reveal the item at the head of the queue
        if there is one, or None if there isn't one"""
        if self.qsize() > 0:
            return self._queue[0]
        return None
