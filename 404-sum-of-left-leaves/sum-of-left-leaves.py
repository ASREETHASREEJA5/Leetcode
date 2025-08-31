# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isleaf(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            return 0
        def dfs(root):
            if not root:
                return 0
            if isleaf(root.left):
                return root.left.val+dfs(root.right)
            else:
                return dfs(root.left)+dfs(root.right)
        return dfs(root)

        