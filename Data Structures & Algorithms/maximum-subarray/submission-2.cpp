class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size(); 
        int dp[1000] = {};
        dp[0] = nums[0];
        int best = dp[0];
        for (int i = 1; i < n; ++i) {
            dp[i] = max({dp[i - 1] + nums[i], nums[i]});
            best = max(best, dp[i]);
        }
        return best;
    }
};
