# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True

            if not leftNode or not rightNode:
                return False
            
            return leftNode.val == rightNode.val and isMirror(leftNode.left, rightNode.right) and isMirror(leftNode.right, rightNode.left) 
            

        return isMirror(root.left, root.right)