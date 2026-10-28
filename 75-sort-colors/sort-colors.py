class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        one = 0
        two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            elif nums[i] == 1:
                one +=1
            else:
                two +=1
        ind = 0
        for i in range(zeros):
            nums[ind] = 0
            ind+=1
        for i in range(one):
            nums[ind] = 1
            ind+=1
        for i in range(two ):
            nums[ind] = 2
            ind+=1