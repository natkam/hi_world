"""Online Judge, problem no. 100

https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36
"""
import sys


def get_cycle_len(n: int) -> int:
    """Replaces the value of `n` with 3n+1 or n/2 until the result equals to 1.

    The value of `n` is replaced with 3n + 1 for odd values of `n`; it is replaced
    with n/2 for even values of `n`.

    Args:
        n: The integer to start the loop with.

    Returns:
        Integer, the cycle length - how many times the `n` value was reassigned before
        1 was attained, including the initial and the final (1) values.
    """
    cycle_len = 1
    while n != 1:
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        cycle_len += 1
    return cycle_len


def get_max_cycle_len(i: int, j: int) -> int:
    max_cycle_len = 1
    for n in range(i, j + 1):
        cycle_len = get_cycle_len(n)
        if cycle_len > max_cycle_len:
            max_cycle_len = cycle_len
    return max_cycle_len


if __name__ == "__main__":
    for line in sys.stdin:
        i, j = line.rstrip("\n").split()
        print(i, j, get_max_cycle_len(int(i), int(j)))
