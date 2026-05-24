class Solution {
public:
    int best = -1000;
    int maxPathSum(TreeNode* root) {
        postorder(root);
        return best;
    }
    int postorder(TreeNode* root) {
        if(!root) return 0;
        int lv = max(postorder(root->left), 0);
        int rv = max(postorder(root->right), 0);
        best = max(best, root->val + lv + rv);
        return max(lv, rv) + root->val;
    }
};