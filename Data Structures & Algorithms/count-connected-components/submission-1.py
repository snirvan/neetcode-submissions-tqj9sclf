class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        map = {i: [] for i in range(n)}
        for n1, n2 in edges:
            map[n1].append(n2)
            map[n2].append(n1)

        #0: 1
        #1: 0, 2
        #2: 1
        #3: 4
        #4: 3

        components = 0
        visited = set()        
        def dfs(node):
            visited.add(node)

            for n in map[node]:
                if n not in visited:
                    dfs(n)

    

        for node in map:
            if node not in visited:
                components += 1
                dfs(node)

        return components

            


    
