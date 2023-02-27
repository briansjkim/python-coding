class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1

        while i < len(nums):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1

            if j == len(nums):
                i += 1
                j = i


# Using dictionary
class Solution2(object):
    def twoSum(self, nums, target):
        visited_nums = {}

        for i in range(len(nums)):
            if nums[i] in visited_nums:
                return [visited_nums[nums[i]], i]
            else:
                visited_nums[target - nums[i]] = i
