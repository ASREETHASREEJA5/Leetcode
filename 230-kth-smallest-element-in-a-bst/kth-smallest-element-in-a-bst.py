# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def inor(root):
            if root is None:
                return
            
            inor(root.left)
            l.append(root.val)
            inor(root.right)
            return l
        
        inor(root)
        return l[k-1]

