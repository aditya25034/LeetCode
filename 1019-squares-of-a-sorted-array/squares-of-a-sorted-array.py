class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.append(nums[i] * nums[i])


        return sorted(lst)
        