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
# lower bound
def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # index of first element >= target
# upper bound
def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left  # index of first element > target
