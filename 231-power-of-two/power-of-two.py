class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return self.power(n)

    def power(self,n):
        if n==1:
            return True
        elif n>1 and n%2==0:
            return self.power(n//2)
        return False