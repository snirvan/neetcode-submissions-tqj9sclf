class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_count =  0
        
        for num in hashset:
            if num-1 not in hashset:
                count = 1
                current_num = num
                while current_num + 1 in hashset:
                    count += 1
                    current_num += 1
                longest_count = max(longest_count,count)
                count = 0
        
        return longest_count