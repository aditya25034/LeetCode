from collections import Counter
from typing import List
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Two bases and two large prime moduli to avoid hash collisions
        BASE1, MOD1 = 1315423911, 10**9 + 7
        BASE2, MOD2 = 2654435761, 10**9 + 9
        
        # Precompute powers for both bases
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow1[i] = (pow1[i - 1] * BASE1) % MOD1
            pow2[i] = (pow2[i - 1] * BASE2) % MOD2

        def has_unique(length: int) -> bool:
            h1 = h2 = 0
            # Build hash for the initial window [0, length - 1]
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
            
            counts = Counter([(h1, h2)])
            
            # Slide the window across the rest of the array
            for i in range(length, n):
                out_val = nums[i - length]
                in_val = nums[i]
                
                # Remove leftmost element and append rightmost element
                h1 = ((h1 - out_val * pow1[length - 1]) * BASE1 + in_val) % MOD1
                h2 = ((h2 - out_val * pow2[length - 1]) * BASE2 + in_val) % MOD2
                
                counts[(h1, h2)] += 1
                
            # Valid if at least one subarray hash appeared strictly once
            return 1 in counts.values()

        # Binary search over possible subarray lengths [1, n]
        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return ans