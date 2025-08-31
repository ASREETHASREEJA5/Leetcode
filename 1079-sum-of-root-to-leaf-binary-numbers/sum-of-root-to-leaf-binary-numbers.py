# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root,path):
            nonlocal ans
            if not root:
                return
            path+=str(root.val)
            if root.left is None and root.right is None:
                ans+=int(path,2)
            dfs(root.left,path)
            dfs(root.right,path)
        dfs(root,"")
        return ans

        