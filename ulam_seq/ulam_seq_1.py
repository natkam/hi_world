""" https://www.codewars.com/kata/ulam-sequences/train/python """
from timeit import timeit
from itertools import combinations
from collections import Counter

def ulam_sequence(u0, u1, n):
    """
    u0 = first number
    u1 = second numberr
    n  = final number of elements in the sequence
    """
    seq = [u0, u1, u0 + u1]
    sums = Counter([a + b for a, b in combinations(seq, 2) if a + b > seq[-1]])

    while len(seq) < n:

        temp_next_term = seq[-1] + seq[-2]
        smaller_sums = []
        for current_sum in sums.keys():
            if current_sum <= seq[-1]:
                smaller_sums.append(current_sum)
                continue

            if sums[current_sum] <= 1 and current_sum < temp_next_term:
                temp_next_term = current_sum

        for s in smaller_sums:
            del sums[s]

        seq.append(temp_next_term)
        sums += Counter({e + temp_next_term: 1 for e in seq[:-1] if e + temp_next_term > seq[-1]})

    return seq

if __name__ == '__main__':
    print(ulam_sequence(1, 2, 5), [1, 2, 3, 4, 6])

    a = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69]
    print(ulam_sequence(1, 2, 20))
    # print(a)

    b = [1, 3, 4, 5, 6, 8, 10, 12, 17, 21, 23, 28, 32, 34, 39, 43, 48, 52, 54, 59, 63, 68, 72, 74, 79, 83, 98, 99, 101, 110,
     114, 121, 125, 132, 136, 139, 143, 145, 152, 161, 165, 172, 176, 187, 192, 196, 201, 205, 212, 216, 223, 227, 232, 234,
     236, 243, 247, 252, 256, 258]
    print(timeit('ulam_sequence(1, 3, 60)', setup='from ulam_seq_1 import ulam_sequence', number=1))
    # print(b)

    print(timeit('ulam_sequence(1, 2, 1500)', setup='from ulam_seq_1 import ulam_sequence', number=1))
