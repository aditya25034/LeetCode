class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_of_digit=0
        prod_of_digit =1
        while n>0:
            a=n%10
            sum_of_digit += a
            prod_of_digit *= a
            n=n//10
        return prod_of_digit -  sum_of_digit