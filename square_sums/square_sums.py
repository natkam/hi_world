"""
https://www.codewars.com/kata/square-sums-simple
https://www.codewars.com/kata/square-sums
"""
import time
from itertools import permutations
from math import sqrt, floor, ceil

from typing import List, Union, Dict, Tuple


## Takes absurdly long time for N > 10 xD (took ~7.5 minutes for N=12)
def naive_square_sums(N: int = 43):
    limit = ceil(sqrt(N))
    available_squares = [
        n ** 2 for n in range(2, limit)
    ]  # 1**2 is too small to be a sum

    for perm in permutations(range(1, N + 1)):
        if all(a + b in available_squares for a, b in zip(perm, perm[1:])):
            print(perm)
            return perm
        else:
            continue
    return False


def prepare_pairs(available_squares: List[int], N: int) -> Dict[int, List[int]]:
    """ For each number in the input, get a list of available complementary numbers. """
    pairs = {}
    for n in range(1, N + 1):
        pairs[n] = [
            sq - n for sq in available_squares if sq - n != n and 0 < sq - n <= N
        ]
    return pairs


def square_sums(N: int = 43):
    # Sum of two numbers in the input list cannot be bigger than (2 * number - 1); thus:
    max_square = floor(sqrt(N + (N - 1))) ** 2
    available_squares = [n ** 2 for n in range(2, max_square + 1)]

    pairs: Dict[int, List[int]] = prepare_pairs(available_squares, N)

    # If any number does not have any complementary numbers, there's no solution:
    if any(len(val) == 0 for val in pairs.values()):
        return False

    # If a number only has one complementary number, it has to be at the beginning or end
    # of the returned sequence. Hence, there cannot be more than two such numbers:
    edge_numbers: List[Tuple[int, List[int]]] = list(
        filter(lambda x: len(x[1]) == 1, pairs.items())
    )
    # wtf, typing... "Expected type 'List[Tuple[int, List[int]]]', got 'List[int]'
    # instead" - nope, you didn't.
    if len(edge_numbers) > 2:
        return False

    if edge_numbers:
        # Solutions are symmetrical, so let's arbitrarily choose a starting number:
        solution = [edge_numbers[0]]
    else:
        solution = []

    # TODO: create solutions from available pairs


def solution_is_correct(number: int, solution: Union[List[int], bool]) -> bool:
    if not solution:
        print(
            f"[N = {number}] WARNING: It's impossible to easily verify that a solution "
            f"does not exist!"
        )
        return True

    all_numbers_used_once = len(set(solution)) == len(solution) == number
    sums_are_correct = all(
        floor(sq) == sq
        for sq in map(lambda a: sqrt(a[0] + a[1]), zip(solution, solution[1:]))
    )
    # print(list(map(sum, zip(solution, solution[1:]))))

    return all_numbers_used_once and sums_are_correct


if __name__ == "__main__":
    # assert solution_is_correct(15, [9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8])
    # assert solution_is_correct(15, square_sums(15))

    for N in range(5, 15):
        assert solution_is_correct(N, square_sums(N))

    assert solution_is_correct(18, square_sums(18))

    # start = time.perf_counter()
    # assert solution_is_correct(12, square_sums(12))
    # print(time.perf_counter() - start)
