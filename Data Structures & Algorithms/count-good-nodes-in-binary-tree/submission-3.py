# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, maxSeen):
            nonlocal count
            if root.val >= maxSeen:
                count += 1
                maxSeen = root.val
            
            if root.left:
                dfs(root.left, maxSeen)
            if root.right:
                dfs(root.right, maxSeen)
            
            
        dfs(root, root.val)
        return count