# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "N"
            return f"({node.val},{serialize(node.left)},{serialize(node.right)})"
        
        rootSerialized = serialize(root)
        subRootSerialized = serialize(subRoot)
        return subRootSerialized in rootSerialized
            
            
            
                
              