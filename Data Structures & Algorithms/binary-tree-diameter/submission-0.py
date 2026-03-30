# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dm = 0
        def height(node):
            nonlocal dm

            if not node:
                return 0
            left_ht = height(node.left)
            right_ht = height(node.right)

            dm = max(dm, left_ht + right_ht)

            return 1 + max(left_ht, right_ht)

        height(root)
        return dm
        

        