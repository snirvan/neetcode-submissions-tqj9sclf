class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
        candidates.sort()
        curSet, combinations = [],[]

        def helper(i, total):
            if total == target:
                combinations.append(curSet.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            curSet.append(candidates[i])
            helper(i + 1, total + candidates[i])
            curSet.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1,total)

        helper(0,0)
        return combinations

    #         [1]      []            
    #     [1,2]   [1]
    # [1,2,2]   [1,2]
        