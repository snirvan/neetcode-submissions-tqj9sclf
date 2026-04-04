class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (right - left) // 2 + left
            col = mid % len(matrix[0])
            row = mid // len(matrix[0])

            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1 
            else:
                right = mid - 1
        
        return False
            
            