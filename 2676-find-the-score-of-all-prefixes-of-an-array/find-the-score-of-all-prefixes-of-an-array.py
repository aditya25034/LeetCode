class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        # conver = []
        # maximum = nums[0]
        # prefix = 0
        # for i in range(len(nums)):
        #     maximum = max(maximum , nums[i])
        #     x = (nums[i]+ maximum)
        #     prefix += x
        #     nums[i] = prefix
        # return nums


        prefix_sum = 0
        maximum = nums[0]
        for i in range(len(nums)):
            if nums[i] > maximum :
                maximum = nums[i]
            number = nums[i] + maximum
            prefix_sum += number
            nums[i] = prefix_sum
        return nums

