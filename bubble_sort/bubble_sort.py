import time
start_clock = time.clock()

def bubble_sort(list_to_sort):
    length = len(list_to_sort)
    for j in range(1, length):
        bubble_up(list_to_sort, j)

def bubble_up(list_to_sort, j):
    length = len(list_to_sort)
    for i in range(length - j):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

list_to_sort = [46, 69, 8, 26, 14, 78, 12, 24]
list_to_sort_worst_case = list(range(10000, 0, -1))

bubble_sort(list_to_sort_worst_case)

print('--- %s seconds ---' % (time.clock() - start_clock))
