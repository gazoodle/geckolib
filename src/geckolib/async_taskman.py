"""GeckoAsyncTaskMan is a wrapper on AsyncTasks with some shared properties."""

from .async_tasks import AsyncTasks


class GeckoAsyncTaskMan(AsyncTasks):
    """Async tasks with spa name and id."""

    unique_id = ""
    spa_name = ""

    def __init__(self) -> None:
        """Initialize the async task manager class."""
        super().__init__()
