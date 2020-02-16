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


def solve(n, pairs, solution, N):
    candidates = [c for c in pairs[n] if c not in solution]

    if not candidates:
        if len(solution) == N - 1:
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

    for number in pairs:
        solution = []
        solution = solve(number, pairs, solution, N)
        if solution:
            print(f"N = {N}, solution = {solution}")
            return solution

    return False

#     ##### Premature optimisation is the root of all evil.  #####
#     # If a number only has one complementary number, it has to be at the beginning or end
#     # of the returned sequence. Hence, there cannot be more than two such numbers:
#     edge_numbers: List[int] = [pair[0] for pair in pairs.items() if len(pair[1]) == 1]
#
#     if len(edge_numbers) > 2:
#         return False
#
#     # if edge_numbers:
#     #     solution = [0 for _ in range(N)]
#     #     # Solutions are symmetrical, so let's arbitrarily choose a starting number:
#     #     solution[0] = edge_numbers[0]
#     #     solution[1] = pairs[solution[0]][0]
#     #     # ...while the other one goes at the end of the solution:
#     #     solution[-1] = edge_numbers[1]
#     #     solution[-2] = pairs[solution[-1]][0]
#     # else:
#     #     solution = []
#
#     solution = []
#     if edge_numbers:
#         # Solutions are symmetrical, so let's arbitrarily choose a starting number:
#         candidate = edge_numbers[0]
#         # TODO: how about the other edge number? Put it at the end? Save it for later:
#         last_number = (edge_numbers[1], pairs.pop(edge_numbers[1]))
#         edge_numbers = []
#     else:
#         # No clue, so we may just as well start from the beginning:
#         # TODO: try other candidates in case this one fails!
#         candidate = pairs[1][0]
#
#     solution.append(candidate)
#     candidates = pairs[solution[-1]]
#     pairs.pop(solution[-1])
#
#     if len(candidates) == 1:
#         # easy-peasy
#         solution.append(candidates[0])
#         next_candidates = pairs[solution[-1]]
#         pairs.pop(solution[-1])
#     else:
#         for val, candidates in pairs.items():
#             pairs[val] = [c for c in candidates if c != solution[-1]]
#             if len(pairs[val]) == 1:
#                 edge_numbers.append(val)


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

    for N in range(5, 16):
        assert solution_is_correct(N, square_sums(N))

    assert solution_is_correct(18, square_sums(18))  # no solution
    # N = 30, solution = [1, 24, 25, 11, 5, 4, 12, 13, 3, 6, 30, 19, 17, 8, 28, 21, 15,
    #   10, 26, 23, 2, 14, 22, 27, 9, 16, 20, 29, 7, 18]
    assert solution_is_correct(30, square_sums(30))
    # N = 31, solution = [1, 15, 10, 6, 30, 19, 17, 8, 28, 21, 4, 5, 31, 18, 7, 29, 20,
    #   16, 9, 27, 22, 3, 13, 12, 24, 25, 11, 14, 2, 23, 26]
    assert solution_is_correct(31, square_sums(31))

    start = time.perf_counter()
    # N = 37, solution = [1, 3, 13, 36, 28, 8, 17, 32, 4, 21, 15, 34, 30, 19, 6, 10, 26,
    #     23, 2, 7, 18, 31, 33, 16, 9, 27, 22, 14, 35, 29, 20, 5, 11, 25, 24, 12, 37]
    assert solution_is_correct(37, square_sums(37))
    print(time.perf_counter() - start)  # 1.3896432460023789
