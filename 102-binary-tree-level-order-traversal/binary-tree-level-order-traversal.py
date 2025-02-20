# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            level = []
            for i in range(size):
                data = q.popleft()
                level.append(data.val)
                if data.left:
                    q.append(data.left)
                if data.right:
                    q.append(data.right)
            ans.append(level)
        return ans

        