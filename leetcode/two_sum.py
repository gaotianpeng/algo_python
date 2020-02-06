from typing import List


def two_sum_a(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums) - 1):
        tmp = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] == (target - tmp):
                return [i, j]


def two_sum_b(nums: List[int], target: int) -> List[int]:
    want = {}
    for i, num in enumerate(nums):
        if num in want:
            return [want[num], i]
        else:
            want[target - num] = i
    return []


# test case
nums = [2, 7, 11, 15]
target = 9

print(two_sum_a(nums, target))
print(two_sum_b(nums, target))