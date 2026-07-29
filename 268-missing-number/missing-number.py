class Solution(object):
    def missingNumber(self, nums):
        curr=0
        for i in range(len(nums)):
            curr = nums[i]^curr
        for j in range(len(nums)+1):
            curr = j^curr
        return curr