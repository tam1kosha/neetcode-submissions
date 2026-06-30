class Solution {
public:
    int jump(vector<int>& nums) {
        int left = 0, right = left;
        int n = nums.size();
        int count = 0;
        while (right < n - 1) {
            int maxJump = 0;
            for (int i = left; i <= right; i++) {
                maxJump = max(maxJump, i + nums[i]);
            }
            left = right + 1;
            right = maxJump;
            count++;
        }
        return count;
    }
};
