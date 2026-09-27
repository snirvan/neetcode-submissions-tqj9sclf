class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a,b = -heapq.heappop(stones), -heapq.heappop(stones)
            if a == b:
                if len(stones) == 0:
                    heapq.heappush(stones,0)
            else:
                heapq.heappush(stones,-(a-b))
        return abs(stones[0])
