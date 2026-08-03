class Solution:
    def reverseString(self, s: List[str]) -> None:
        nums =s
        l=0
        r=len(s)-1
        while l<=r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l+=1
            r-=1
        