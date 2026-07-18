class Solution:
    def minElement(self, nums: List[int]) -> int:
        lst =[]
        i=0
        while i<len(nums):
            digit_sum = 0
            for digit in str(nums[i]): 
                digit_sum += int(digit)
            lst.append(digit_sum)
            i+=1
        return min(lst)