class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        s=set()
        for num in nums:
            s.add(num)
        
        for i in range(1,len(nums)+1):
            if i not in s:
                return i
        
        return len(nums)+1
        