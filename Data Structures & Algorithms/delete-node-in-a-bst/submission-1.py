# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# find the node 1) no children 2) 1 child , return that child
        # 3) 2 children, copy the inorder sucessor and then delete that
        

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None 
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        # == key 
        else:
            if not root.left and not root.right: return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # 2 children, update with sucessor , delete but keep rest of the subtree
            sucessor = self.get_min(root.right)
            root.val = sucessor.val
            root.right = self.deleteNode(root.right, sucessor.val)

        return root

    def get_min(self, node:TreeNode):
        while node.left:
            node = node.left
        return node
             


        
        
