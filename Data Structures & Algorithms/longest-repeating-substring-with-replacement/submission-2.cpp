class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0, right = left;
        int res = 0;
        int n = s.size();
        unordered_map<char, int> hmp;
        int max_count = 1;
        hmp[s[right]]++;
        while(right < n) {
            int len = right - left + 1;
            if (len - max_count <= k) {
                res = max(res, len);
                right++;
                hmp[s[right]]++;
                max_count = max(max_count, hmp[s[right]]);
            }
            else {
                hmp[s[left]]--;
                left++;
            }
        }
        return res;
    }
};
