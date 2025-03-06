"""Unit tests for the AsyncPeekableQueue ."""  # noqa: INP001

# ruff: noqa: E501

from geckolib.driver.async_peekablequeue import AsyncPeekableQueue


class TestAsyncPeekableQueue:
    """Tests for async peekable queue."""

    def test_empty_on_construction(self) -> None:
        q = AsyncPeekableQueue()
        assert not q.is_data_available
        assert not q
        assert len(q) == 0

    def test_with_state(self) -> None:
        q = AsyncPeekableQueue()
        q.push(1)
        q.push(2)
        assert q.is_data_available
        assert q
        assert len(q) == 2
        one = q.pop()
        assert q.is_data_available
        assert one == 1
        assert q
        assert len(q) == 1
        two = q.pop()
        assert two == 2
        assert not q.is_data_available
        assert not q
        assert len(q) == 0

    def test_command_priority(self) -> None:
        q = AsyncPeekableQueue()
        q.push(1)
        q.push(2)
        q.push(3)
        q.push_command(4)
        assert len(q) == 4
        assert q.peek() == 4
        four = q.pop()
        assert four == 4
        assert q.is_data_available
        assert q.peek() == 1
