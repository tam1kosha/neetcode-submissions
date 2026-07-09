class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return nums[0];
        
        return max({
            robFirst(nums, n),
            robLast(nums, n),
            robNeither(nums, n)
        });
    }

    int robFirst(vector<int> nums, const int& n) {
        if (n == 2) return max(nums[0], nums[1]);
        nums[n - 1] = 0;
        int dp[100] = {};
        dp[0] = nums[0];
        dp[1] = max(nums[1], nums[0]);
        for (int i = 2; i < n; ++i) {
            dp[i] = max({
                dp[i - 2] + nums[i],
                dp[i - 1]
            });
        }
        return dp[n - 1];
    }

    int robLast(vector<int>& nums, const int& n) {
        if (n == 2) return max(0, nums[1]);
        int dp[100] = {};
        dp[0] = 0;
        dp[1] = nums[1];
        for (int i = 2; i < n; ++i) {
            dp[i] = max({
                dp[i - 2] + nums[i],
                dp[i - 1]
            });
        }
        return dp[n - 1];
    }

    int robNeither(vector<int>& nums, const int& n) {
        if (n == 2) return 0;
        int dp[100] = {};
        dp[0] = 0;
        dp[1] = nums[1];
        for (int i = 2; i < n - 1; ++i) {
            dp[i] = max({
                dp[i - 2] + nums[i],
                dp[i - 1]
            });
        }
        return dp[n - 2];
    }
};
