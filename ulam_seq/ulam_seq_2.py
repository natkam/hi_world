import time
from collections import Counter


def ulam_sequence(u0, u1, n):
    """
    u0: first number
    u1: second number
    n: final number of elements in the sequence
    """
    seq = [u0, u1, u0 + u1]
    sums = Counter([2 * u0 + u1, u0 + 2 * u1])

    while len(seq) < n:
        seq_max = seq[-1]
        sums_copy = sums.copy()
        temp_next_term = seq[-1] + seq[-2]

        for key, val in sums_copy.items():
            if key <= seq_max:
                del sums[key]
                continue

            if val > 1:
                continue

            if key < temp_next_term:
                temp_next_term = key

        seq.append(temp_next_term)
        sums += Counter(
            {e + temp_next_term: 1 for e in seq[:-1] if e + temp_next_term > seq[-1]}
        )

    return seq


if __name__ == "__main__":
    start = time.perf_counter()
    [ulam_sequence(1, 3, 60) for _ in range(1000)]  # ca. 3.3 second (1000 times)
    print(
        f"----- ulam_sequence(1, 3, 60): {(time.perf_counter() - start)} seconds (1000 times) -----"
    )
    start = time.perf_counter()
    ulam_sequence(1, 2, 1500)  # ca. 2.6 second
    print(
        f"----- ulam_sequence(1, 2, 1500): {time.perf_counter() - start} seconds -----"
    )
