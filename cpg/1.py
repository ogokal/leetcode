from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, num in enumerate(nums):
            diff = target - num
            diffs[diff] = i

        for i, num in enumerate(nums):
            if num in diffs:
                if i != diffs[num]:
                    return [i, diffs[num]]
