class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive =[]
        negative =[]
        for i in range(len(nums)):
            if nums[i] >0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        nums[0] = positive[0]
        for i in range(1,len(nums)):
            if i%2 == 0:
                nums[i] = positive[i//2]
            else:
                nums[i] = negative[i//2]

        return nums
            