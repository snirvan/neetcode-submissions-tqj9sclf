class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #product of non zeros
        prod = 1
        zeros = 0
        arr_len = len(nums)

        for num in nums:
            if num != 0:
                prod *= num
            else:
                zeros += 1
        
        if zeros >= 2:
            return [0] * arr_len
        
        result = [0] * arr_len
        for i in range(arr_len):
            if zeros == 1:
                if nums[i] == 0:
                    result[i] = prod
                else:
                    result[i] = 0
            else:
                result[i] = prod // nums[i]
        
        return result
        
    
       #case1: no zeros: every number is product / num
       #case2: 1 zero: only value of 0 is set as product everything else set to 0
       #case3: 2 or more zeros: return array of 0s



        