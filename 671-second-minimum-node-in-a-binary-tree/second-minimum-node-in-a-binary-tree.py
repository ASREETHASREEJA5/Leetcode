# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans1 = sys.maxsize
        def dfs(root):
            nonlocal ans1
            if not root or (root.left is None and root.right is None):
                return
            ans = max(root.left.val,root.right.val) 
            if ans != root.val:
                ans1 = min(ans,ans1)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        if ans1 == sys.maxsize:
            return -1
        return ans1
        