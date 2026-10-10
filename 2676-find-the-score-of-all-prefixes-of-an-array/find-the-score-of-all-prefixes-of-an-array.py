class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        conver = []
        maximum = nums[0]
        prefix = 0
        for i in range(len(nums)):
            maximum = max(maximum , nums[i])
            x = (nums[i]+ maximum)
            prefix += x
            nums[i] = prefix
        return nums