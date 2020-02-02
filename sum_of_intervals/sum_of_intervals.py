""" https://www.codewars.com/kata/sum-of-intervals """
import time
from random import randint
from typing import List


def sum_of_intervals_1(intervals: List[List[int]]) -> int:
    intervals.sort()
    merged = []
    previous = intervals[0]

    for interval in intervals[1:]:
        if previous[1] >= interval[0]:
            previous = [previous[0], max(previous[1], interval[1])]
        else:
            merged.append(previous)
            previous = interval
    merged.append(previous)

    return sum(i[1] - i[0] for i in merged)


def sum_of_intervals_2(intervals: List[List[int]]) -> int:
    s = set()
    _ = [s.update(range(*interval)) for interval in intervals]
    return len(s)


def prepare_inputs(n: int = 10000):
    intervals = []
    for _ in range(n):
        interval = []
        for i in range(randint(10, 500)):
            s = randint(1, 200)
            e = s + randint(1, 50)
            interval.append([s, e])
        intervals.append(interval)
    return intervals


if __name__ == "__main__":
    assert sum_of_intervals_2([[1, 2], [6, 10], [11, 15]]) == 9
    assert sum_of_intervals_2([[1, 4], [7, 10], [3, 5]]) == 7
    assert sum_of_intervals_2([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]) == 19

    perf_tests = prepare_inputs()

    start_1 = time.perf_counter()
    for test_case in perf_tests:
        sum_of_intervals_1(test_case)
    print(f"1st solution: {time.perf_counter() - start_1}")

    start_2 = time.perf_counter()
    for test_case in perf_tests:
        sum_of_intervals_2(test_case)
    print(f"2nd solution: {time.perf_counter() - start_2}")
    # both solutions have comparable execution times, though the 1st one seems to be
    # slightly faster (~10%)
