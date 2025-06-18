# binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # inclusive range
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # target found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # not found
