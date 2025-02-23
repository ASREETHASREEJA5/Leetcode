# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        # Create root from first element of preorder
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root  # Base case (single node)

        # Find left subtree size using postorder
        left_subtree_root = preorder[1]  # Left child is always preorder[1]
        left_subtree_size = postorder.index(left_subtree_root) + 1  # Find left child's index in postorder

        # Recursively construct left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_subtree_size + 1], postorder[:left_subtree_size])
        root.right = self.constructFromPrePost(preorder[left_subtree_size + 1:], postorder[left_subtree_size:-1])
        return root