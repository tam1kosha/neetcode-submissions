class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> hs;
        for (const int& num : nums)
        {
            hs.insert(num);
        }
        int best = 0;
        for (auto& key : hs)
        {
            if(!hs.contains(key - 1)){
                int temp = 0;
                while(hs.contains(key + temp)) temp++;
                if(temp > best) best = temp;
            }
        }
        return best;
    }
};
