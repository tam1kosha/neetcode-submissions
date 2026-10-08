class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        int m = s2.size();
        if (n > m) return false;

        unordered_map<char, int> hmp1, hmp2;
        for (int i = 0; i < n; i++) {
            hmp1[s1[i]]++;
            hmp2[s2[i]]++;
        }

        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (hmp1[i + 'a'] == hmp2[i + 'a']) matches++;
        }

        for (int i = n; i < m; i++) {
            if (matches == 26) return true;

            hmp2[s2[i]]++;
            if(hmp1[s2[i]] == hmp2[s2[i]]) matches++;
            else if(hmp1[s2[i]] + 1 == hmp2[s2[i]]) matches--;

            
            hmp2[s2[i - n]]--;
            if(hmp1[s2[i - n]] == hmp2[s2[i - n]]) matches++;
            else if(hmp1[s2[i - n]] - 1 == hmp2[s2[i - n]]) matches--;

        }
        return matches == 26;
    }
};
