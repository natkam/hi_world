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
    # TODO: memoization? For bigger N, more options can be added. Would it make sense?
    pairs = {}
    for n in range(1, N + 1):
        pairs[n] = [
            sq - n for sq in available_squares if sq - n != n and 0 < sq - n <= N
        ]
    return pairs


def solve(n, pairs, solution, N):
    candidates = [c for c in pairs[n] if c not in solution]

    if not candidates:
        if len(solution) == N - 1:  # all candidates already used
            solution.append(n)
            return solution
        return False

    solution.append(n)

    for c in candidates:
        succeeded = solve(c, pairs, solution, N)
        if succeeded:
            return solution

    solution.pop()
    return False


def square_sums(N: int = 43):
    # Sum of two numbers in the input list cannot be bigger than (2 * number - 1); thus:
    max_square = floor(sqrt(N + (N - 1))) ** 2
    available_squares = [n ** 2 for n in range(2, max_square + 1)]

    pairs: Dict[int, List[int]] = prepare_pairs(available_squares, N)

    # If any number does not have any complementary numbers, there's no solution:
    if any(len(val) == 0 for val in pairs.values()):
        return False

    ### This trick only helps with small N's, apparently there's no edge numbers for N>30 :(
    # If a number only has one complementary number, it has to be at the beginning or end
    # of the returned sequence. Hence, there cannot be more than two such numbers:
    edge_numbers: List[int] = [pair[0] for pair in pairs.items() if len(pair[1]) == 1]

    if len(edge_numbers) > 2:
        return False

    if edge_numbers:
        print(f"\t[N = {N}] Edge numbers found! {edge_numbers}")
        # Solutions are symmetrical, so let's arbitrarily choose a starting number:
        solution = []
        solution = solve(edge_numbers[0], pairs, solution, N)
        if solution:
            print(f"N = {N}, solution = {solution}")
            return solution
    else:
        for number in pairs:
            solution = []
            solution = solve(number, pairs, solution, N)
            if solution:
                print(f"N = {N}, solution = {solution}")
                return solution

    return False


def solution_is_correct(number: int, solution: Union[List[int], bool]) -> bool:
    if not solution:
        print(
            f"[N = {number}] No solution found.\n"
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
    for N in range(5, 15):
        assert square_sums(N) is False

    for N in set(range(18 - 25)) - {23}:
        assert square_sums(N) is False  # no solution

    # N = 15, solution = [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9]
    # N = 16, solution = [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9, 16]
    # N = 17, solution = [16, 9, 7, 2, 14, 11, 5, 4, 12, 13, 3, 6, 10, 15, 1, 8, 17]
    # N = 23, solution = [2, 23, 13, 12, 4, 21, 15, 10, 6, 19, 17, 8, 1, 3, 22, 14, 11,
    #   5, 20, 16, 9, 7, 18]
    # N = 30, solution = [1, 24, 25, 11, 5, 4, 12, 13, 3, 6, 30, 19, 17, 8, 28, 21, 15,
    #   10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18]
    # N = 31, solution = [1, 15, 10, 6, 30, 19, 17, 8, 28, 21, 4, 5, 31, 18, 7, 29, 20,
    #   16, 9, 27, 22, 3, 13, 12, 24, 25, 11, 14, 2, 23, 26]
    # N = 37, solution = [1, 3, 13, 36, 28, 8, 17, 32, 4, 21, 15, 34, 30, 19, 6, 10, 26,
    #     23, 2, 7, 18, 31, 33, 16, 9, 27, 22, 14, 35, 29, 20, 5, 11, 25, 24, 12, 37]

    for N in [15, 16, 17, 23, 30, 31, 37]:
        start = time.perf_counter()
        assert solution_is_correct(N, square_sums(N))
        print(f"[N = {N}] {time.perf_counter() - start}")  # ~ 0.77-1.4 s for N=37

    # N = 48, solution = [1, 3, 6, 10, 15, 21, 4, 32, 17, 47, 2, 34, 30, 19, 45, 36, 28,
    #   8, 41, 40, 9, 7, 29, 20, 16, 48, 33, 31, 18, 46, 35, 14, 11, 5, 44, 37, 27, 22,
    #   42, 39, 25, 24, 12, 13, 23, 26, 38, 43], took >40 seconds
    # N = 49, ...
    # N = 50, solution = [1, 3, 6, 10, 15, 21, 43, 38, 26, 23, 2, 7, 18, 46, 35, 29, 20,
    #   44, 37, 12, 13, 36, 28, 8, 41, 40, 24, 25, 39, 42, 22, 27, 9, 16, 48, 33, 31, 50,
    #   14, 11, 5, 4, 45, 19, 30, 34, 47, 17, 32, 49], still it took almost 7 minutes :D
    
    # for N in range(38, 51):
    #     start = time.perf_counter()
    #     assert solution_is_correct(N, square_sums(N))
    #     print(f"[N = {N}] {time.perf_counter() - start}")