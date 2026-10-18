# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # postorder rule: 2 operator waiting for 1 operand 
        if not root.left and not root.right:
            return root.val == 1
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        if root.val == 2: 
            return left or right
        else:
            return left and right
        
