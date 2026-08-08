class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i,n in enumerate(nums):
            hm[n] = i

        result = []
        for i,n in enumerate(nums):
            compliment = target - n

            if compliment in hm and hm[compliment] != i: 
                result.extend([i,hm[compliment]])
                return result
        return result


    # hashmap of compliment: index
