# LC twoSum
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1

        while p1 < len(nums):
            if nums[p1] + nums[p2] == target:
                return [p1, p2]
            else:
                p2 += 1

            if p2 == len(nums):
                p1 += 1
                p2 = p1 + 1


# Using hash map
class HashSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}

        for i in range(len(nums)):
            if nums[i] in visited_nums:
                return [visited_nums[nums[i]], i]
            else:
                visited_nums[target - nums[i]] = i
