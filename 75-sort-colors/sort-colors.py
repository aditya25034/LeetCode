class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            is_swap = False
            for j in range(len(nums)-i-1):

                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                    is_swap = True
                
            if not is_swap:
                return
        