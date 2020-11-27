import asyncio

import pytest

from .coro_decorator import run_with_lock


@pytest.mark.asyncio
async def test_coroutine_called_twice_gets_locked():
    dict_with_key_a = {"a": 5}

    @run_with_lock()
    async def add_to_a(dict_with_key_a, number: int = 1, sleep_time: int = 1):
        await asyncio.sleep(sleep_time)
        dict_with_key_a["a"] += number
        return dict_with_key_a["a"]

    await asyncio.gather(
        add_to_a(dict_with_key_a, number=1, sleep_time=3),
        add_to_a(dict_with_key_a, number=4, sleep_time=1),
    )

    assert dict_with_key_a["a"] == (5 + 1) + 4


@pytest.mark.asyncio
async def test_two_distinct_coroutines_do_not_get_locked():
    dict_with_key_a = {"a": 5}

    @run_with_lock()
    async def add_three_to_a_slowly(dict_with_key_a):
        await asyncio.sleep(3)
        dict_with_key_a["a"] += 3
        return dict_with_key_a["a"]

    @run_with_lock()
    async def multiply_a_by_two_quickly(dict_with_key_a):
        await asyncio.sleep(1)
        dict_with_key_a["a"] *= 2
        return dict_with_key_a["a"]

    await asyncio.gather(
        add_three_to_a_slowly(dict_with_key_a),
        multiply_a_by_two_quickly(dict_with_key_a),
    )

    assert dict_with_key_a["a"] == (5 * 2) + 3


@pytest.mark.asyncio
async def test_two_distinct_coroutines_with_same_lock():
    dict_with_key_a = {"a": 5}

    lock = asyncio.Lock()

    @run_with_lock(lock)
    async def add_three_to_a_slowly(dict_with_key_a):
        await asyncio.sleep(3)
        dict_with_key_a["a"] += 3
        return dict_with_key_a["a"]

    @run_with_lock(lock)
    async def multiply_a_by_two_quickly(dict_with_key_a):
        await asyncio.sleep(1)
        dict_with_key_a["a"] *= 2
        return dict_with_key_a["a"]

    await asyncio.gather(
        add_three_to_a_slowly(dict_with_key_a),
        multiply_a_by_two_quickly(dict_with_key_a),
    )

    assert dict_with_key_a["a"] == (5 + 3) * 2
