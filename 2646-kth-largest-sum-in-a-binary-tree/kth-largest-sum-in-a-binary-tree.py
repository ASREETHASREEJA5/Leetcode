# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        ans = []
        while q:
            c = 0
            for i in range(len(q)):
                node = q.popleft()
                c+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(c)
        ans.sort()
        print(ans)
        if k>len(ans):
            return -1
        return ans[-k]

        