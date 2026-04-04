class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        card_count = {}
        for x in hand:
            card_count[x] = card_count.get(x,0) + 1
        
        minheap = list(card_count.keys())
        heapq.heapify(minheap)

        while minheap:
            smallest = minheap[0]

            for i in range(smallest, smallest+groupSize):
                if i in card_count:
                    card_count[i] -= 1
                    if card_count[i] == 0:
                        heapq.heappop(minheap)
                else:
                    return False

        return True



# use minheap
# count all cards
# while hands not empty:
#   take first item in array 
#   for range(first, first + groupsize)
#       check if in hashmap, if it is decrement by 1
#           and remove from array
#       if it isn't return False
#       
# return True