# Init solution; however, it doesn't work with 0s + shouldn't use division
class Solution(object):
    def productExceptSelf(self, nums):
        product = 1
        answer = []

        for num in nums:
            product *= num

        for num in nums:
            if num != 0:
                res = product / num
                answer.append(res)

        return answer

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer