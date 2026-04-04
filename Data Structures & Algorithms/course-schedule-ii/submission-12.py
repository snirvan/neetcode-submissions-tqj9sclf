class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        visited = set()
        cycle = set()
        result = []

        crsMap = {i: [] for i in range(numCourses)}

        # 0: [1]
        # 1: [2]
        # 2: []

        # result: 2, 1, 0
        # visited: 0

        # dfs(0) 

        for crs, prereq in prerequisites:
            crsMap[crs].append(prereq)

        def dfs(crs):
            # result.append(crs)
            # # if crs in visited return empty
            # if crs in visited:
            #     return False
            # visited.add(crs)
            # # if crs is not visited 
            #     #  if crs has no prereq add to possible ordering
            # if crsMap[crs] == []:
            #     continue
            # # explore crs with prereq, add to result
            # for prereq in crsMap[crs]:
            #     dfs(prereq) 

            # if no prereq, then add to result
            # if prereq, check if all prereq in result
                # if prereq not in result
                    # dfs(prereq that is not in result)
            #add crs to result
            
            # visited.add(crs)
            # if crsMap[crs] == []:
            #     result.append(crs)
            #     return
            
            # for prereq in crsMap[crs]:
            #     if prereq not in result and prereq in visited:
            #         return False    
            #     if prereq not in result and prereq not in visited:
            #         if dfs(prereq) == False:
            #             return False


            
            # result.append(crs)
            # return
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for prereq in crsMap[crs]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(crs)
            visited.add(crs)
            result.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return result


# 0: 
# 1: 2
# 2: 1

# result: 
# visited: 0, 1, 


# result: 0, 1, 2
# visited: 

# dfs(0) return 
# dfs(1) return
# dfs(2)  return
        

#[0,1] [0,2] [0,3], [2,3]

# 0: 1,2,3
# 1: 
# 2: 3
# 3: 

# result: 1,3,2,0
# visited: 1,3,2,0




