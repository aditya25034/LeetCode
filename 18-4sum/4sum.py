class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                p= j+1
                q = len(nums)-1
                while p<q:
                    curr = nums[i] + nums[j] + nums[p] + nums[q]
                    if curr == target:
                        ans.add(tuple((nums[i] , nums[j] , nums[p] , nums[q])))
                        p+=1
                        q-=1
                    elif curr < target:
                        p+=1
                    else:
                        q-=1
        return list(ans)