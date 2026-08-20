class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search form 1 to max of max(piles)
        # pick mid point 
        # iterate through piles 
        # time += ciel(p/k)

        # if time > h: min = mid + 1
        # if time <= h: compare with current best time if its smaller than set best_k=mid and then move to max = mid - 1


        left = 1
        right = max(piles)
        best_k = right

        while left <= right:
            mid = (right-left) //2 + left
            time = 0

            for pile in piles:
                time += math.ceil(pile/mid)
            
            if time > h:
                left = mid + 1
            else:
                best_k = min(best_k,mid)
                right = mid - 1
        
        return best_k
                


