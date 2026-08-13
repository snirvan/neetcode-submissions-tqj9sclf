class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build hashmap num -> count
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        #build min heap and push num,count 
        heap = []
        for num,freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        
        return result
        