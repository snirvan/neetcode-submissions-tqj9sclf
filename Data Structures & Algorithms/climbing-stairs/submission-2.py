class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array = [None] * (n+1)
        def dfs(n):
            if n <= 3:
                dp_array[n] = n
                return n
            elif dp_array[n] is not None:
                return dp_array[n]

            dp_array[n] = dfs(n-1) + dfs(n-2)
            return dp_array[n]
        
        return dfs(n)