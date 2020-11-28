"""Online Judge, problem no. 100

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36
"""
import sys


def get_cycle_len(n: int) -> int:
    """Replaces the value of `n` with 3n+1 or n/2 until the result equals to 1.

    The value of `n` is replaced with 3n + 1 for odd values of `n`; it is replaced
    with n/2 for even values of `n`.
    The function uses pre-computed values of `cycle_len` from the global dict
    `computed_cycle_lens`, if an already computed `n` is reached in the loop.

    Args:
        n: The integer to start the loop with.

    Returns:
        Integer, the cycle length - how many times the `n` value was reassigned before
        1 was attained, including the initial and the final (1) values.
    """
    global computed_cycle_lens
    initial_n = n

    cycle_len = 1
    while n != 1:
        if n in computed_cycle_lens:
            cycle_len += computed_cycle_lens[n] - 1
            break
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        cycle_len += 1

    return computed_cycle_lens.setdefault(initial_n, cycle_len)


def get_max_cycle_len(i: int, j: int) -> int:
    """Finds maximum cycle length for all ints between `i` and `j`, `i` and `j` included.

    Does not assume that `i` is smaller than `j`.
    """
    i, j = sorted([i, j])
    max_cycle_len = 0
    for n in range(i, j + 1):
        cycle_len = get_cycle_len(n)
        if cycle_len > max_cycle_len:
            max_cycle_len = cycle_len
    return max_cycle_len


if __name__ == "__main__":
    computed_cycle_lens = dict()
    for line in sys.stdin:
        i, j = line.rstrip("\n").split()
        print(i, j, get_max_cycle_len(int(i), int(j)))
