class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l+= 1
        
        return nums
        



# have two points l, r
# l should be zero 
# incrament r until it reaches last index
# whenever r is non zero swap it with l

#