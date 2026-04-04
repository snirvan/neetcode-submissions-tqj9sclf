# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p and q < root: LCA is in the left subtree
        # if p and q > root: LCA is in the right subtree
        # if one of them is < root and the other is > root: the root is the LCA CHECK
        # if root == p or q: p or q is the LCA

        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root
        if (root.val == p.val):
            return p
        if (root.val == q.val):
            return q
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        return self.lowestCommonAncestor(root.right,p,q)
        
        