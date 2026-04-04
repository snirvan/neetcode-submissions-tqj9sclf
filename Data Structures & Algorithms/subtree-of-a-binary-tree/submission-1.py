# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(r,sr):
            if r == None and sr == None:
                return True
            if r and sr and r.val == sr.val:
                return sameTree(r.left, sr.left) and sameTree(r.right, sr.right)
            else:
                return False

        q = collections.deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.val == subRoot.val and sameTree(node, subRoot):
                        return True
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return False
