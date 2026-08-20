class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # combine into one array and then do binary search
        l = 0
        r = len(matrix) * len(matrix[0]) - 1

        while l <= r:
            mid = (r-l) //2 + l

            rows = mid // len(matrix[0])
            cols = mid % len(matrix[0])

            val = matrix[rows][cols]

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
        
        return False



        
    # rows = n // 4
    # cols = n % 4