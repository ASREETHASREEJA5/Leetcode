# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = defaultdict(list)
        q = deque([(root, 0, 0)])   
        while q:
            node, row, col = q.popleft()
            nodes[col].append((row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))
        ans = []
        for col in sorted(nodes.keys()):
            column_nodes = sorted(nodes[col], key=lambda x: (x[0], x[1]))
            ans.append([val for _, val in column_nodes])      
        return ans