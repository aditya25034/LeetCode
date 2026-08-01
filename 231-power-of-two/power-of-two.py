class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif n>1 and n%2==0:
            return self.isPowerOfTwo(n//2)
        return False

        