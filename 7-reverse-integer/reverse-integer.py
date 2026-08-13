class Solution:
    def reverse(self, x: int) -> int:
        b=0
        a=x
        if x<0:
            x=x*(-1)
            
        while x>0:
            b = (b*10)+ (x%10)
            x= x//10

        if b<(-2**31) or b>((2**31)-1):
            return 0
        
        if a<0:
            return b*(-1)
        
        return b