class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        done = set()
        preMap = {i: [] for i in range(numCourses)} 

        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        def dfs(crs):
            if crs in visiting:
                return False

            if preMap[crs] == []:
                return True

            visiting.add(crs)

            for prereq in preMap[crs]:
                if prereq in done:
                    continue
                elif dfs(prereq) == False:
                    return False
            
            visiting.remove(crs)
            done.add(crs)
            return True

        for crs in preMap.keys():
            if dfs(crs) == False:
                return False
        
        return True


                