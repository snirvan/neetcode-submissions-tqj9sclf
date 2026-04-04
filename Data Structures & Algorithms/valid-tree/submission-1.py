class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # no cycle
            # run dfs starting from one node and make sure no node is repeated
        # all nodes connected 
            # when node visited add to set to make sure all nodes are connected


        #0: 1, 2, 3 
        #1: 0,4
        #2: 0
        #3: 0
        #4: 1

        visited = set()
        map = {i: [] for i in range(n)}   
        
        for n1, n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)
        
        print(map)

        allNodes = set()
        # for i in range(n):
        #     allNodes.add(i)
        
        # print(allNodes)

        def dfs(parent, node):
            if node in allNodes:
                return False
            allNodes.add(node)
            if node in visited:
                return False
            
            visited.add(node)

            for nodes in map[node]:
                if nodes != parent:
                    if dfs(node,nodes) == False:
                        return False

            visited.remove(node)
            return True


        # for node in map:
        #     if dfs(node) == False:
        #         return False
        
        if dfs(None,0) == False:
            return False

        if len(allNodes) != n:
            return False
        
        return True

        # return dfs(0) and len(allNodes) != 0

#0: 1
#1: 0,2,3,4
#2: 1,3
#3: 2,1
#4: 1


