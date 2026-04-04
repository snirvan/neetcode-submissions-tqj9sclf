class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations, curSet = [],[]

        def helper(i, curSet, combinations, total):

            if total == target:
                combinations.append(curSet.copy())
                return

            if i >= len(nums) or total > target:
                return 

            curSet.append(nums[i])
            helper(i, curSet, combinations, total + nums[i])
            curSet.pop()
            helper(i+1, curSet, combinations, total)
        
        helper(0, curSet, combinations, 0)
        return combinations
            
