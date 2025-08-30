# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        c = 0
        def trv(root):
            nonlocal c
            if root is None:
                return
            trv(root.left)
            trv(root.right)
            c+=1
        trv(root)
        return c
        