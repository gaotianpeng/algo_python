from typing import List
# Binary search
def bserarch(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

def bsearch_internally(nums:List[int], low:int, high:int, target: int)->int:
    if low > high:
        return -1

    mid = low + int((high-low) >> 1)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return bsearch_internally(nums, mid+1, high, target)
    else:
        return bsearch_internally(nums, low, mid-1, target)
    return -1

def bsearch_recur(nums: List[int], target: int) -> int:
    return bsearch_internally(nums, 0, len(nums) - 1, target)
## test case
test_nums = []
for i in range(10):
    test_nums.append(i+1)
print(test_nums)
print(bserarch(test_nums, 6))
print(bsearch_recur(test_nums, 6))





