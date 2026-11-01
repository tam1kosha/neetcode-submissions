# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {val: i for i, val in enumerate(inorder)}

        def build(preL, preR, inL, inR):
            if preL > preR:
                return None

            root_val = preorder[preL]
            mid = index_of[root_val]        # root's position in inorder
            left_size = mid - inL           # number of nodes in left subtree

            root = TreeNode(root_val)
            # left subtree: preorder [preL+1 .. preL+left_size], inorder [inL .. mid-1]
            root.left = build(preL + 1, preL + left_size, inL, mid - 1)
            # right subtree: preorder [preL+left_size+1 .. preR], inorder [mid+1 .. inR]
            root.right = build(preL + left_size + 1, preR, mid + 1, inR)
            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

        

    


        

