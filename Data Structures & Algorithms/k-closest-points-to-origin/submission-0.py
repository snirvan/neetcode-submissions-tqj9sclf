class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for x,y in points:
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(maxheap,(-distance, (x,y)))
        
        while len(maxheap) > k:
            heapq.heappop(maxheap)
        
        output = []
        for distance,(x,y) in maxheap:
            output.append([x,y])

        return output

# make maxheap
# traverse through points, calculate euclidan distance and store in maxheap distances[i] = (points[i], distance)
# heapify distance array into a max heap


# 5,4,2,3

# while len(max heap) > k:
    # pop 

# iterate thorugh maxheap
# add items to output array
# return output array