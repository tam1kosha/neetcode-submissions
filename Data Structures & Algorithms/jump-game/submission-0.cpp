class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int goal = n - 1;
        int curr = n - 2;
        while (curr >= 0) {
            if(goal <= curr + nums[curr]) {
                goal = curr;
                curr--;
            }
            else curr--;
        }
        return goal == 0;
    }
};
