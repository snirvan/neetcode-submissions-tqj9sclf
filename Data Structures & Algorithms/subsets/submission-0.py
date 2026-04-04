class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(i, nums, curSet, subsets):
            #past numsRange, then end
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            #add 
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subsets)
            curSet.pop()
            #dont add
            helper(i+1, nums, curSet,subsets)

        curSet, subsets = [], []
        helper(0,nums, curSet, subsets)
        return subsets

        