## Big O -- O(n^2) worst, O(n) best


def insertion_sort(seq):
    size = len(seq)

    if size <= 0:
        return seq

    for idx in range(1, size):
        prev = idx
        temp = seq[idx]

        while prev > 0 and temp < seq[prev - 1]:
            seq[prev] = seq[prev - 1]
            prev -= 1

        seq[prev] = temp

    return seq


seq1 = [2, 4, 7, 3, 6, 234, 1, 7, 9, 11, 6, 1, -5, 18, 55, 192]

# simulation:
# 0: [2, 4, 7, 3]
# 1: [2, 4, 7, 7] temp: 3
# 2: [2, 4, 4, 7] temp: 3
# 3: out of while loop: temp: 3, prev: 1 -> seq[1] = 3 -> [2, 3, 4, 7]

print(insertion_sort(seq1))
