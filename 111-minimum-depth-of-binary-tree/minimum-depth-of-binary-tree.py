# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def hei(root):
            if root is None:
                return 0
            if not root.left:
                return(1+hei(root.right))
            if not root.right:
                return(1+hei(root.left))
            return (1+(min(hei(root.left),hei(root.right))))
        return hei(root)
        