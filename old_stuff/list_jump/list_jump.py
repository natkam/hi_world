def solution(list_to_jump):
    list_len = len(list_to_jump)
    if list_len == 0:
        print("an empty list!")
        return 0
    if list_len > 100000:
        print("this is way to much!")
        return 0
    current_position = 0
    jump_length = 1 # zeby nie byl == 0
    counter = 0

    while (jump_length != 0) :
        if current_position >= list_len or current_position < 0:
            return counter
        jump_length = list_to_jump[current_position]
        list_to_jump[current_position] = 0
        current_position += jump_length
        counter += 1

    return -1

aa = [1, 2, 1, -12, -12]
print(solution(aa))
