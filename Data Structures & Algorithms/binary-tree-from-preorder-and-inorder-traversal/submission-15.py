# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder - {head, [leftsubtree], [rightsubtree]}
        # inorder - {[leftsubtree], head, [rightsubtree]}
        # to solve this task we need to figure why we are given both order types to build a tree. Why we cannot do it with only one order type?
        # let's say we want to use only preorder type, then how do we know at which point leftsubtree ends? well without using other order type you cannot do that. 
        """
            how to use the inorder type then? we know that leftsubtree ends right before current head of a subtree will appear in a list, hence we can recursively call buildTree function with preorder[leftsubtree], and inorder[leftsubtree] and say that resulting subtree will belong to left pointer of the current head, and subsequently, right pointer will take the result of preorder[rightsubtree] and inorder[rightsubtree]. two main question yet to be answered: how to define base cases and how to effectively divide both order type lists to left and rightsubtrees.
        """
        # if len(preorder) == 0 or len(inorder) == 0:
        #     return None
        # if len(preorder) == 1 or len(inorder) == 1:
        #     return TreeNode(preorder[0], None, None)

        # head = preorder[0]
        
        # index = 0
        # while inorder[index] != head:
        #     index += 1
        
        # left_inorder = inorder[:index]
        # right_inorder = inorder[index + 1:]

        # left_preorder = preorder[1:index + 1]
        # right_preorder = preorder[index + 1:]

        # curr = TreeNode(head, self.buildTree(left_preorder, left_inorder), self.buildTree(right_preorder, right_inorder))

        # return curr

        """
        after initial approach i got stuck with TLE issues, and i assume it is because i keep copying lists, switching to shrinking index approach. Here in amin function we. could intialize parameters for the new index based function.
        """
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

        

    


        

