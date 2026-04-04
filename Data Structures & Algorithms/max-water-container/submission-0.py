class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        left = 0
        right = len(heights) - 1
        
        while left < right:
            curVol = (right - left) * min(heights[left], heights[right])
            if curVol > maxVol:
                maxVol = curVol

            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
        return maxVol
        


# maxVol
# (r - l) * min(heights[l],  heights[r])
# if min(heights[l],  heights[r]) == heights[l]:
#   l+1
# else:
#   r-1

# l             r
# 1,7,2,5,4,7,3,6