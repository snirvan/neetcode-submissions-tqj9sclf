class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l = 0 r=len(heights)-1

        # while l<r
        #area = min(nums[l],nums[r]) * (r-l)
        # if nums[l] < nums[r]: l+= 1
        # if nums[l] >= nums[r]: r-=1

        l=0
        r = len(heights)-1
        largest = 0

        while l < r:
            area = min(heights[l],heights[r]) * (r-l)
            largest = max(area,largest)

            if heights[l]< heights[r]:
                l+= 1
            else:
                r -= 1

        return largest