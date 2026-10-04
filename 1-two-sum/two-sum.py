class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        # nums.sort()
        # res = []
        # i=0
        # j=len(nums)
        # while True:
        #     if nums[i]+nums[j] == target:
        #         return i,j
        #     elif nums[i]+nums[j]>target:
        #         j-=1
        #     else:
        #         i+=1
        for i in range(len(nums)):
            hash_map[nums[i]] = i
        print(hash_map)

        for i in range(len(nums)):
            a= target - nums[i]
            if a in hash_map and hash_map[a] != i:
                return hash_map[a] , i    
                