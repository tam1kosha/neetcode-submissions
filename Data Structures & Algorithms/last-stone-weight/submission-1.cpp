class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> mpq;
        for (int stone : stones) mpq.push(stone);
        int n = stones.size();
        while (n > 1 && !mpq.empty()) {
            int x = mpq.top();
            mpq.pop();
            int y = mpq.top();
            mpq.pop();
            if (x != y) mpq.push(abs(x - y));
            n--;
        }
        return mpq.empty()? 0 : mpq.top();
    }
};
