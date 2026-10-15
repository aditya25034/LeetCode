class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        ans = set()
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            target = nums[i] *(-1)

            if nums[i+1] + nums[i+2] > target:
                break 
            
            if nums[n-1] + nums[n-2] < target:
                continue
            j=i+1
            k=n-1
            target = nums[i] *(-1)

            while j<k:
                if nums[j] + nums[k] == target:
                    ans.add((nums[i] , nums[j] , nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > nums[i] *(-1):
                    k-=1
                else:
                    j+=1

        return [lst for lst in ans]