from typing import List
# 查找第一个等于给定值的元素
def bsearch_first_equal(nums: List[int], target: int) -> int :
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                high = mid - 1

# 查找最后一个值等于给定值的元素
def bsearch_last_equal(nums: List[int], target: int) -> int:
    low, high, n = 0, len(nums) - 1 , len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            if mid == n or nums[mid+1] != target:
                return mid
            else:
                low = mid + 1
    return -1

# 查找第一个大于等于给定值的元素
def bsearch_first_not_less(nums: List[int], target) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] >= target:
            if mid == 0 or nums[mid-1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1

# 查找最后一个小于等于给定值的元素
def bsearch_less_not_greater(nums: List[int], target: int):
    low, high , n = 0, len(nums) - 1, len(nums) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if nums[mid] > target:
            high = mid - 1
        else:
            if mid == n or nums[mid+1] > target:
                return mid
            else:
                low = mid + 1
    return -1

###############################################
## test
test_data = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
print(bsearch_first_equal(test_data, 5))
print(bsearch_last_equal(test_data, 5))
print(bsearch_first_not_less(test_data, 7))
print(bsearch_less_not_greater(test_data, 8))
