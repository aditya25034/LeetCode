class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n= len(nums)
        hash_map = {}
        for i in range(n):
            hash_map[nums[i]] = hash_map.get(nums[i] , 0)+1
            if hash_map[nums[i]] > (n/2):
                return nums[i]