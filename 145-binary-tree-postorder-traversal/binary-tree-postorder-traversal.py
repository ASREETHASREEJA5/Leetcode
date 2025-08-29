# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        curr = root
        lastVisited = None

        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                # if right child exists and not visited
                if peek.right and lastVisited != peek.right:
                    curr = peek.right
                else:
                    result.append(peek.val)  # visit node
                    lastVisited = stack.pop()

        return result

        