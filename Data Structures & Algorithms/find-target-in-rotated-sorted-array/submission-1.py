class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1 
            else:
                R = mid
        
        if target >= nums[L] and target <= nums[len(nums)-1]:
            l = L
            r = len(nums) -1
        else:
            l = 0
            r = L 
        
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1


        


        







        # L = 4
        # R = 3
        # mid = 


        #real index: (3 + 4 % 6)

        # 1,2,3,4,5,6 
        # 6,1,2,3,4,5 if mid less than both sides: go to the left
        # 5,6,1,2,3,4 
        # 3,4,5,6,1,2 if mid greater than both sides: go to the right

