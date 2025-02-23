# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def diam(root):
            if root is None:
                return 0
            lh = diam(root.left)
            rh = diam(root.right)
            self.diameter = max(self.diameter,lh+rh)
            return 1 + max(lh,rh)
        diam(root)
        return self.diameter
        