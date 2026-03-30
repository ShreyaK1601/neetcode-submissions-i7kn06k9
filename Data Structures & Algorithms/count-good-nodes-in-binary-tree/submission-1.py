# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.gnCount = 0
        
        def dfs(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                self.gnCount += 1
            
            new_max_val = max(max_val, node.val)

            dfs(node.left, new_max_val)
            dfs(node.right, new_max_val)

        if not root:
            return
        
        dfs(root, root.val)

        return self.gnCount
        
        
        # # Initialize a counter for good nodes
        # self.good_nodes_count = 0

        # # Helper DFS function
        # def dfs(node, max_val_on_path):
        #     # Base case: if the node is None, stop
        #     if not node:
        #         return

        #     # Check if the current node is a "good node"
        #     # It's good if its value is greater than or equal to the maximum
        #     # value encountered on the path from the root to this node.
        #     if node.val >= max_val_on_path:
        #         self.good_nodes_count += 1
            
        #     # Update the maximum value seen on the path for subsequent calls
        #     # The new max for children will be the greater of current max_val_on_path
        #     # and the current node's value.
        #     new_max_val_on_path = max(max_val_on_path, node.val)
            
        #     # Recursively call for left and right children
        #     dfs(node.left, new_max_val_on_path)
        #     dfs(node.right, new_max_val_on_path)
        
        # # Handle the edge case of an empty tree
        # if not root:
        #     return 0

        # # Start the DFS from the root.
        # # The root itself is always a good node, so we initialize max_val_on_path with root.val.
        # # This ensures the root is correctly counted and its value becomes the initial max.
        # dfs(root, root.val)
        
        # # Return the total count of good nodes
        # return self.good_nodes_count
        