# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # This is the approach, basically follow a ranged search (x < y < z) for this
        # algorithm, any value to the right of a node should have it's left range updated because
        # it has to be greater than that of the provided value, for any value to the left of a given
        # tree, we'll need to update the right range 

        def isvalid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return (isvalid(node.left, left, node.val) and 
            isvalid(node.right, node.val, right))

        return isvalid(root, float("-inf"), float("inf"))            



