class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums) - 1
        while L < R:
            mid = (L + R) // 2
            if nums[mid] > nums[R]:
                L = mid + 1 
            else:
                R = mid
        

        if target <= nums[-1] and target >= nums[L]:
            l = L
            r = len(nums)-1
        else:
            l = 0
            r = L-1
        
        while l <= r:
            mid = (r-l)//2 + l
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid + 1
        
        return -1