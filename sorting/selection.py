## Big O - O(n^2) worst, O(n^2) best
## Always iterates through the whole sequence even if it's already sorted
## returning a non-decreasing sequence

def selection_sort(seq):
    size = len(seq)

    if size <= 0:
        return seq

    for idx in range(size):
        min_ = idx

        for n in range(idx + 1, size):
            if seq[n] < seq[min_]:
                min_ = n

        seq[min_], seq[idx] = seq[idx], seq[min_]

    return seq


seq1 = [2, 4, 6, 6, 234, 1, 7, 9, 11, 6, 1, -5, 18, 55, 192]

print(selection_sort(seq1))




