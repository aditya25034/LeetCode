class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        window_sum = 0
        ans = 0
        for i in range(k):
            window_sum += arr[i]
            avg = window_sum / k
        if avg >= threshold :
                ans+=1
        for i in range(k,len(arr)):
            window_sum += arr[i]
            window_sum -= arr[i-k]
            avg = window_sum /k
            if avg>=threshold:
                ans+=1
        return ans