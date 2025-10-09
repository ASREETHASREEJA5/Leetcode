# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = []
        while q:
            l = []
            for i in range(len(q)):
                node = q.pop(0)
                l.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(l[-1].val)
        return res
        