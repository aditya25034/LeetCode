class Solution:
    def canJump(self, nums: list[int]) -> bool:
        i = 0
        max_index = 0
        n = len(nums)
        while i<n:
            if i> max_index :
                return False
            if (i+nums[i]) > max_index:
                max_index = i+ nums[i]
            if max_index >= n:
                return True
            i+=1
        return True