""" https://www.codewars.com/kata/sum-of-intervals """


def sum_of_intervals(intervals):
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


if __name__ == "__main__":
    assert sum_of_intervals([[1, 2], [6, 10], [11, 15]]) == 9
    assert sum_of_intervals([[1, 4], [7, 10], [3, 5]]) == 7
    assert sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]) == 19
