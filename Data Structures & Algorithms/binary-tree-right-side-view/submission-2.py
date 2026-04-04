# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        q = collections.deque()
        q.append(root)
        while q:
            ql = len(q)
            level = []
            for i in range(ql):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    level.append(node.val)
            if len(level) is not 0:
                ans.append(level[-1])
        
        return ans

        # level: 2,3
        # ans 1,3
        # q: 
        # node: 1