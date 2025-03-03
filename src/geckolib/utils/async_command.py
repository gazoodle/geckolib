"""AsyncCmd class."""

import asyncio
import cmd
import logging
import threading
from queue import Empty, Queue
from typing import Any, Self

_LOGGER = logging.getLogger(__name__)


class AsyncCmd(cmd.Cmd):
    """
    AsyncCmd. Async command processor based on cmd.Cmd.

    This class will run an async loop in a thread and all the async
    functions will run in there, including any do_ commands in the
    derived shell that are decorated with the async keyword.
    """

    prompt = "(async-cmd) "

    def __init__(self) -> None:
        """Initialize the async class."""
        super().__init__()
        self.queue: Queue[tuple] = Queue()
        self.stop_event: threading.Event = threading.Event()
        self.thread: threading.Thread = threading.Thread(
            target=self.run_async_loop, daemon=True
        )
        self.thread.start()

    def __enter__(self) -> Self:
        """Suport python 'with' syntax."""
        _LOGGER.debug("Start shell %s", self.__class__.__name__)
        return self

    def __exit__(self, *exc_info: object) -> None:
        """Suport puthon 'with' syntax."""
        _LOGGER.debug("Stop shell %s", self.__class__.__name__)

    def run_async_loop(self) -> None:
        """Run the async loop."""
        _LOGGER.debug("Running async loop")
        with asyncio.Runner() as runner:
            runner.run(self.process_commands())

    async def process_commands(self) -> None:
        """Process command loop."""
        aenter = self.__getattribute__("__aenter__")
        if aenter is not None:
            _LOGGER.debug("Calling aenter %s", aenter)
            await aenter()

        try:
            while not self.stop_event.is_set():
                try:
                    coroutine, args = self.queue.get(timeout=0.01)
                    _LOGGER.debug("Run coroutine %s with %s", coroutine, args)
                    await coroutine(*args)
                    self.queue.task_done()
                except Empty:
                    await asyncio.sleep(0)
                except asyncio.CancelledError:
                    _LOGGER.debug("Command loop cancelled")
                    raise
                except Exception:
                    _LOGGER.exception("Command loop exception, logged and continue")
        finally:
            aexit = self.__getattribute__("__aexit__")
            if aexit is not None:
                _LOGGER.debug("Calling aexit %s", aexit)
                await aexit()

    def dispatch(self, coroutine: Any, *args: Any) -> None:
        """Dispatch a command the async loop."""
        self.queue.put_nowait((coroutine, args))

    def precmd(self, line: str) -> str:
        """Determine if the command is running in the io loop, or async loop."""
        parts = line.split(" ", 1)
        command_name: str = parts[0]
        rest: str = parts[1] if len(parts) > 1 else ""
        method: Any | None = getattr(self, f"do_{command_name}", None)
        if asyncio.iscoroutinefunction(method):
            self.dispatch(method, rest)
            return ""
        return line

    def do_exit(self, _line: str) -> bool:
        """Stop the async loop and exits the program."""
        self.stop_event.set()
        self.thread.join()
        return True
