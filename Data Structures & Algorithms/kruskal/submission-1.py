class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.height = [0] * n

        for i in range(n):
            self.par[i] = i
    
    def find(self, x: int) -> int:
        # Finds the root of x
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p 
    
    def union(self, x: int, y: int) -> bool:
        # Connects x and y
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        
        if self.height[root_x] < self.height[root_y]:
            self.par[root_x] = root_y
        elif self.height[root_y] < self.height[root_x]:
            self.par[root_y] = root_x
        else:
            self.par[root_x] = root_y
            self.height[root_y] +=1
            
        return True 

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # Use a min heap to sort the edges
        minHeap = []
        for n1, n2, weight in edges:
            heapq.heappush(minHeap,[weight,n1,n2])
        # Use Union Find to keep track of the connected components
        unionFind = UnionFind(n)

        res = 0
        components = n
        # Pop the edges from the min heap and connect the nodes
        while minHeap and components > 1:
            weight, n1, n2 = heapq.heappop(minHeap)
            if unionFind.union(n1,n2):
                res += weight
                components -= 1

        # Return -1 if not all nodes are visited (unconnected graph)
        if components == 1:
            return res
        return -1