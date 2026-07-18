class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max =0
        i=0
        j=i+1
        while j<len(prices):
            if prices[i]<prices[j]:
                profit = prices[j]-prices[i]
                curr_max = max(curr_max , profit)
                
            else:
                i=j
            j+=1
        return curr_max