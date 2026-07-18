class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i , n in enumerate(nums):
            differ = target - n
            if differ in hashmap:
                return [hashmap[differ] , i]
            hashmap[n] = i
        return       