class Solution:
    def findMin(self, nums: List[int]) -> int:
        # l = 0
        # r = len(nums) - 1
        # mid = (r-l)//2 +l 

        # if nums[mid] > nums[r]: then min is to the right
        # if nums[mid] < nums[r]: then min is to the left or the current number is the min

        l = 0
        r = len(nums)-1
        while l < r:
            mid = (r-l) //2 + l

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        return nums[r]


        # 5,6,1,2,3,4

        #l=2
        #r=2
        #mid = 1