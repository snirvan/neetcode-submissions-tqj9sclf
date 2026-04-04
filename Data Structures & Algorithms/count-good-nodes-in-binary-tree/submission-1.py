# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    import sys
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(curr,maxNode=-sys.maxsize-1):
            count = 0 
            if curr == None:
                return 0 

            if curr.val >= maxNode:
                count = 1
            maxNode = max(maxNode,curr.val)
            
            count += (dfs(curr.right,maxNode) + dfs(curr.left, maxNode))
            return count

        
        return dfs(root)
                        # count: 3
                        #maxNode: 2
    
    # count: 1                          # count: 1
    # maxNode: 3                        # maxNode: 4    