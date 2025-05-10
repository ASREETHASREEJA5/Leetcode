

class Solution:
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            node = TreeNode(value)
            if value < stack[-1].val:
                # Left child case
                stack[-1].left = node
            else:
                # Find parent for right child
                parent = None
                while stack and value > stack[-1].val:
                    parent = stack.pop()
                parent.right = node

            stack.append(node)

        return root
