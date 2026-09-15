class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        lst =[]
        for i in range(len(nums)-k , len(nums)):
            lst.append(nums[i])
        nums[:] = lst + nums[:len(nums)-k]
        return nums