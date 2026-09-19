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

            # add current courses to visiting
            visiting.add(crs)
            # explore all prereqs
            for prereq in preMap[crs]:
                if prereq in done:
                    continue
                if dfs(prereq) == False:
                    return False
            # remove current course from visiting
            visiting.remove(crs)
            done.add(crs)
            return True

        for crs in range(numCourses):
            if dfs(crs) == False:
                return False

        return True


                