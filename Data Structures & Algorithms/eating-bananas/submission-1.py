class Solution:
    import math
    import sys

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # upper bound of k = max value in piles
        # time per pile = ceil (x/k)

        # range 1 to max value in piles 

        min_val = 1
        max_val = max(piles)
        curr = max_val
        curr_val = sys.maxsize

        while min_val <= max_val:
            mid = (max_val - min_val) // 2 + min_val
            time = 0
            for i in range(0,len(piles)):
                time += math.ceil(piles[i]/mid)
            
            if time > h:
                min_val = mid + 1
            elif time <= h:
                max_val = mid - 1
                curr = mid
                # if mid < curr and time < curr_val:
                #     curr,curr_val = mid, time
        return curr

        # h = 9
        # min = 1
        # max = 1
        # mid = 2
        # time = 6
        # curr = 4
        # curr_val = 