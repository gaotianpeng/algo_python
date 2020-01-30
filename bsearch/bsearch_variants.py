from typing import List
# 查找第一个等于给定值的元素
def bsearch_left_first(nums: List[int], target: int) -> int :
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
def bsearch_right_last(nums: List[int], target: int) -> int:
    # low, high = 0, len(nums) -1
    pass
#

# 查找第一个大于等于给定值的元素
def bsearch_left_not_less():
    pass

# 查找最后一个小于等于给定值的元素
def bsearch_right_not_greater():
    pass


###############################################
## test
test_data = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
print(bsearch_left_first(test_data, 5))
