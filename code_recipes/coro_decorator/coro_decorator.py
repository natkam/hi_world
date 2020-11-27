import asyncio
import typing


def run_with_lock(
    lock: asyncio.Lock = None
) -> typing.Callable[..., typing.Callable[..., typing.Awaitable]]:
    """Decorator that adds a lock on the decorated coroutine.

    The point of the decorator is to prevent the same coroutine from being
    ran more than once at the same time. If you run a decorated coroutine twice
    at the same time, the second call will wait until the first call is
    finished. If you call two different decorated coroutines, they get
    different Lock objects, and can be executed asynchronously.

    There's also a possibility to force two different decorated coroutines to
    use the same lock, by passing the lock object as the decorator argument.

    IMPORTANT: The decorated coroutine cannot be run with `asyncio.run`!
    `asyncio.run` creates a new event loop, and it will raise a RuntimeError.
    Use `asyncio.get_event_loop().run_until_complete` instead.
    """
    lock = lock or asyncio.Lock()

    def lock_decorator(coro: typing.Callable[..., typing.Awaitable]) -> typing.Callable:
        async def locked_coro(*args, **kwargs):
            async with lock:
                return await coro(*args, **kwargs)

        return locked_coro

    return lock_decorator


async def example():
    # TODO: add an example; for now, see the tests
    pass


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
