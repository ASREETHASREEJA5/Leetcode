# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        def dfs(node,par=None):
            if not node:
                return
            parent[node] = par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root)

        q = deque([(target,0)])
        seen = set([target])
        res = []
        while q:
            node,dist = q.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for i in (node.left,node.right,parent[node]):
                    if i and i not in seen:
                        seen.add(i)
                        q.append((i,dist+1))
        return res
