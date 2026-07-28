class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_element = 0
        second_max= 0
        for i in nums:
            if i >=max_element:
                second_max = max_element
                max_element = i
            else:
                if i >second_max:
                    second_max = i
        ans = (max_element-1) * (second_max-1)
        return ans