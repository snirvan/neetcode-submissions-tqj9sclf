class Solution:
    import sys
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = sys.maxsize

        

        
        while l < r:
            mid = (r - l) // 2 + l
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
        


# 1 2 3 4 5 6
# l   m     r              l <= m <= r:  return 1st item

# 6 1 2 3 4 5
# l   m     r              l> m and m < r and l < r --> go left

# 5 6 1 2 3 4               
# l   m     r               

# 4 5 6 1 2 3
# l   m     r               l < m and m > r and l > r --> go right


# 3 4 5 6 1 2               l < m and m > r and l > r --> go right
# l   m     r 


# 2 3 4 5 6 1               l < m and m > r --> go right
# l   m     r 