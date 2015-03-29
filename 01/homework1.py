aa = [1, 2, 1, -12, -12]


def solution(A):
    N = len(A)
    
    if N == 0:
        print("an empty array!")
        return 0
    
    if N > 100000:
        print("this is way to much!")
        return 0
    
    current_position = 0
    jump_length = 1 # zeby nie byl == 0
    counter = 0
        
    while (jump_length != 0) :
        if current_position >= N or current_position < 0:
            #print("out of range")
            return counter
        #print(counter, current_position, A[current_position])
        
        jump_length = A[current_position]
        A[current_position] = 0
        #print(A)
        current_position += jump_length
        counter += 1
    
    return -1

print(solution(aa))
