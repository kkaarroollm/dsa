## Divide and Conquer - divide problems onto small ones, then solve smaller problems


def binary_search(seq, key):
    # returns index of a target key
    # it manipulates the index of the sequence, which are increasing
    low_idx = 0
    high_idx = len(seq) - 1

    while low_idx <= high_idx:
        mid_idx = (high_idx + low_idx) // 2

        if seq[mid_idx] < key:
            low_idx = mid_idx + 1

        elif seq[mid_idx] > key:
            high_idx = mid_idx - 1

        else:
            return mid_idx

    return -1


seq1 = [2, 4, 6, 7, 9, 11, 15, 18, 55, 192, 234]

print(binary_search(seq1, 234))
