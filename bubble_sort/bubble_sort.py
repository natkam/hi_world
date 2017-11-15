list_to_sort = [46, 69, 8, 26, 14, 78, 12, 24]
list_to_sort_worst_case = []
for num in range(10, 0, -1):
    list_to_sort_worst_case.append(num)

def bubble_up(list_to_sort, j):
    length = len(list_to_sort)
    for i in range(length - j):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]

def bubble_sort(list_to_sort):
    print('list_to_sort = ' + str(list_to_sort))
    length = len(list_to_sort)
    for j in range(1, length):
        bubble_up(list_to_sort, j)
    print('sorted list: ' + str(list_to_sort))

bubble_sort(list_to_sort)
bubble_sort(list_to_sort_worst_case)
