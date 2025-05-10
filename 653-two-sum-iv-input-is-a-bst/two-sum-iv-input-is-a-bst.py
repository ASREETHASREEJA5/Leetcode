# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        def preo(root):
            if root is None:
                return
            l.append(root.val)
            preo(root.left)
            preo(root.right)
        preo(root)
        for i in l:
            if k-i in l:
                if k-i == i:
                    if l.count(i)>1:
                        return True
                else:
                    return True

        return False