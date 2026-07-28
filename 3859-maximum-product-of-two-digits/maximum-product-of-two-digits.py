class Solution:
    def maxProduct(self, n: int) -> int:
        x=0
        y=0
        for i in str(n):
            if i>str(x):
                y=x
                x=i
            else:
                if i>str(y):
                    y=i
        return int(x)*int(y)
        