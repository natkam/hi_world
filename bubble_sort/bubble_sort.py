import random
import time


def bubble_sort(list_to_sort):
    for j in range(1, len(list_to_sort)):
        bubble_up(list_to_sort, j)


def bubble_up(list_to_sort, j):
    for i in range(len(list_to_sort) - j):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]


list_to_sort = [random.randint(0, 10000) for _ in range(5000)]
list_to_sort_worst_case = list(range(5000, 0, -1))


if __name__ == "__main__":
    start_clock = time.perf_counter()
    bubble_sort(list_to_sort)
    bubble_sort(list_to_sort_worst_case)
    print("--- %s seconds ---" % (time.perf_counter() - start_clock))
