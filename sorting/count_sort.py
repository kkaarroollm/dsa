# Big O - best - worst: O(k + n)


def counting_sort(seq):
    #### Doesnt work ####
    size = len(seq)
    count = [0] * (max(seq) + 1)

    for n in range(size):
        count[seq[n]] += 1

    sorted_arr = []
    for value, freq in enumerate(count):
        sorted_arr.extend([value] * freq)

    return sorted_arr


seq1 = [2, 4, 6, 6, 234, 1, 7, 9, 11, 6, 1, -5, 18, 55, 192]
print(counting_sort(seq1))
