class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n= len(nums)
        ans = set()
        nums.sort()
        for i in range(n-2):
            j=i+1
            k=n-1
            while j<k:
                if nums[j] + nums[k] == nums[i] *(-1):
                    ans.add((nums[i] , nums[j] , nums[k]))
                    j+=1
                    k-=1
                elif nums[j] + nums[k] > nums[i] *(-1):
                    k-=1
                else:
                    j+=1

        return [lst for lst in ans]