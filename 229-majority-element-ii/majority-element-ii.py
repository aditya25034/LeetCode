class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        hashmap = {}
        n=len(nums)
        hashset = set()
        x=n/3
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i] , 0) +1
        for i in hashmap:
            if hashmap[i] > x:
                hashset.add(i)
        return list(hashset)