class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        diff = float("inf")
        ans = 0
        n= len(nums)
        nums.sort()
        for i in range(n):
            j= i+1
            k=n-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return curr_sum
                elif curr_sum > target:
                    if abs(curr_sum - target) < diff:
                        diff = abs(curr_sum - target)
                        ans = curr_sum
                    k-=1
                else:
                    if abs(curr_sum - target) < diff:
                        diff = abs(curr_sum - target)
                        ans = curr_sum
                    j+=1
        return ans