def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix:
        return False
    target_matrix = None
    i = 0

    while i <= len(matrix) - 1:
        if matrix[i][-1] >= target:
            target_matrix = matrix[i]
            break
        i += 1

    if not target_matrix:
        return False

    high = len(target_matrix)
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if target == target_matrix[mid]:
            return True
        elif target > target_matrix[mid]:
            low = low + 1
        else:
            high = mid - 1

    return False


matrix = [[1]]
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]


print(searchMatrix(matrix, 2))
