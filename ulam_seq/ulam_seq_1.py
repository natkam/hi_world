""" https://www.codewars.com/kata/ulam-sequences/train/python """

from itertools import combinations

def ulam_sequence(u0, u1, n):
    """
    u0 = first number
    u1 = second numberr
    n  = final number of elements in the sequence
    """
    seq = [u0, u1, u0 + u1]

    while len(seq) < n:
        sums = []
        temp_next_terms = []
        for a, b in combinations(seq, 2):
            current_sum = a + b

            if current_sum <= seq[-1]:
                continue

            if current_sum in sums:
                try:
                    temp_next_terms.remove(current_sum)
                except ValueError:
                    pass
                continue

            sums.append(current_sum)
            temp_next_terms.append(current_sum)

        seq.append(min(temp_next_terms))

    return seq

print(ulam_sequence(1, 2, 5))
print([1, 2, 3, 4, 6])

a = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69]
print(ulam_sequence(1, 2, 20))
print(a)

b = [1, 3, 4, 5, 6, 8, 10, 12, 17, 21, 23, 28, 32, 34, 39, 43, 48, 52, 54, 59, 63, 68, 72, 74, 79, 83, 98, 99, 101, 110,
 114, 121, 125, 132, 136, 139, 143, 145, 152, 161, 165, 172, 176, 187, 192, 196, 201, 205, 212, 216, 223, 227, 232, 234,
 236, 243, 247, 252, 256, 258]
print(ulam_sequence(1, 3, 60))
print(b)
