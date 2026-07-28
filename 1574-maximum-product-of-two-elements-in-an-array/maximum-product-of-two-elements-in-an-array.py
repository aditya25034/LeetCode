class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 0
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                maximum = (nums[i]-1) * (nums[j]-1)
                curr_max = max(curr_max, maximum)
                j+=1
            i+=1
        return curr_max