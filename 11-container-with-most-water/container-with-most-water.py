class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0
        # l =0
        # r= len(height)-1
        # while l < r:
        #     area = min(height[l], height[r]) * (r-l)
        #     max_area = max(max_area , area)

        #     if height[l]<height[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return max_area


        maximum =0
        i =0
        j=len(height) -1
        while i<j:
            water = (j-i) * min(height[i] , height[j])
            if water > maximum :
                maximum = water
            if height[i] < height[j] :
                i+=1
            else:
                j-=1
        return maximum