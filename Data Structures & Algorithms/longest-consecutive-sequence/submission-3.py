class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of all numbers
        # iterate through set 
        # if n-1 is not in set:
            # set count to 1
            # start checking if n+1, n+2, n+3... are in the set:
                # keep incramenting count until n+x not in set
            # once loop breaks longest = max(longest,count)
        
        ns = set(nums)
        count = 0
        longest = 0
        for n in ns:
            if n-1 not in ns:
                count = 1
                current = n
                i = 1
                while current + i in ns:
                    count += 1
                    i += 1
                longest = max(longest,count)
                count = 0
        
        return longest



        
            

        

