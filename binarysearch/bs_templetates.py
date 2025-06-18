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

# bs binary_search_answer funstion

def binary_search_answer(low, high, is_valid):
    while low < high:
        mid = (low + high) // 2
        if is_valid(mid):  # condition function
            high = mid
        else:
            low = mid + 1
    return low  # smallest value satisfying is_valid()

# bs  binary_search_real for float point

def binary_search_real(low, high, is_valid, eps=1e-6):
    while high - low > eps:
        mid = (low + high) / 2
        if is_valid(mid):
            high = mid
        else:
            low = mid
    return low

# bs search_rotated_array 

def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # left part is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right part is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
