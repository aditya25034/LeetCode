class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        res =[0] * len(nums)
        p,n = 0,1
        for i in range(len(nums)):
            if nums[i] >0:
                res[p] = nums[i]
                p+=2
            else:
                res[n] = nums[i]
                n+=2
        return res