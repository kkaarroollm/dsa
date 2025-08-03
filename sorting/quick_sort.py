# Big O - O(n * log n)


def quick_sort(seq, start, end):
    if start >= end:
        return

    pivot = partition(seq, start, end)
    quick_sort(seq, start, pivot - 1)
    quick_sort(seq, pivot + 1, end)


def partition(seq, start, end) -> int:
    # returns new pivot for the given array
    pivot = seq[end]
    i = start - 1  # start at -1 position

    for idx in range(start, end + 1):
        if seq[idx] < pivot:
            i += 1  # moving to the next comparing position
            # temp = seq[i]
            # seq[i] = seq[idx]
            # seq[idx] = temp
            seq[i], seq[idx] = seq[idx], seq[i]

    # last loop like won't change last element with the previous if bigger, so have to do it again
    # variable i here, points the idx where old pivot is swapped, if any bigger number, meaning reassigning new pivot
    # putting on the left side smaller numbers and on the right side any bigger the initial pivot
    i += 1
    # temp = seq[i]
    # seq[i] = seq[end]
    # seq[end] = temp
    seq[i], seq[end] = seq[end], seq[i]

    return i


seq1 = [2, 4, 6, 6, 234, 1, 7, 9, 11, 6, 1, -5, 18, 55, 192]

start_ = 0
end_ = len(seq1) - 1

quick_sort(seq1, start_, end_)

print(seq1)
