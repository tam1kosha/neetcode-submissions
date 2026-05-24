class KthLargest {
public:
    priority_queue<int> max_priority_queue;
    int top;
    KthLargest(int k, vector<int>& nums) {
        for (int num : nums) {
            max_priority_queue.push(num);
        }
        top = k;
    }
    
    int add(int val) {
        vector<int> nums;
        max_priority_queue.push(val);
        for (int i = 1; i < top; ++i) {
            nums.push_back(max_priority_queue.top());
            max_priority_queue.pop();
        }
        int ans = max_priority_queue.top();
        for (int num : nums) {
            max_priority_queue.push(num);
        }
        return ans;
    }
};
