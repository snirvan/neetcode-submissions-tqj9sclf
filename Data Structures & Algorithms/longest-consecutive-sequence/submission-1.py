class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])

        longest_count =  0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                count = 1
                current_num = nums[i]
                while current_num + 1 in hashset:
                    count += 1
                    current_num += 1
                longest_count = max(longest_count,count)
                count = 0
        
        return longest_count