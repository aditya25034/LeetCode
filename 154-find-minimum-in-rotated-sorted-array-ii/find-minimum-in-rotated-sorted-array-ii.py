class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) -1
        ans = nums[0]
        while low<high:
            mid = (low + high) //2
            if nums[low] == nums[mid] == nums[high]:
                low +=1
                high -=1
                ans = min(nums[low] , ans)
                continue
            if nums[mid] < nums[low]:
                high = mid-1
                ans = min(nums[mid] , nums[high])
            elif nums[high]<nums[mid]:
                low = mid+1
                ans = min(nums[low] , nums[mid])
            else:
                high = mid-1
        return ans