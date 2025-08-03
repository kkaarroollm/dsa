## Big O -- O(n log n) best, O(n log n) worst


def _merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]

    if j < len(right):
        result += right[j:]

    return result


def merge_arrays_sort(seq):
    # space complex with arrays - O(n) - has to create new arrays
    size = len(seq)

    if size <= 1:
        return seq

    mid = size // 2
    left = seq[:mid]
    right = seq[mid:]

    sorted_left = merge_arrays_sort(left)
    sorted_right = merge_arrays_sort(right)
    return _merge(sorted_left, sorted_right)


seq1 = [2, 4, 7, 3, 6, 234, 1, 7, 9, 11, 6, 1, -5, 18, 55, 192]
print(merge_arrays_sort(seq1))


# space complex with linked list - O(1)


def merge_linked_lists_sort(head):
    pass
