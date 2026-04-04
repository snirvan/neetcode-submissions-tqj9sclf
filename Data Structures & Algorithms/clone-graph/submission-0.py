"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copies = {}
        queue = deque()
        copies[node] = Node(node.val)
        queue.append(node)
        
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in copies:
                    neighbor_copy = Node(neighbor.val)
                    copies[neighbor] = neighbor_copy
                    copies[curr].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
                else:
                    copies[curr].neighbors.append(copies[neighbor])

        return copies[node]



# hashmap
# queue
# add og node to hashmap and queue
# while queue:
# go through queue get curr node iterate through all neighbors 
# add all neighbors to the hashmap and push og to queue and append copy to curr node copy

        