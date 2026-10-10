class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high =len(nums)-1
        # mid = (low+high)//2
        lb = -1
        ub = -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    lb = mid
                high = mid-1
            else:
                low = mid+1
        low =0
        high = len(nums) -1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    ub = mid
                low = mid + 1
            else:
                high = mid -1
        return lb ,ub

            