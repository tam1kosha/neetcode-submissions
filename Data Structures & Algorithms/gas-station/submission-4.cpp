class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> net;
        int n = gas.size();
        vector<int> cumsum(1, 0);
        for (int i = 0; i < n; ++i) {
            net.push_back(gas[i] - cost[i]);
            cumsum.push_back(gas[i] - cost[i] + cumsum.back());
        }

        if (cumsum.back() < 0) return -1;
        for (int i = 0; i < n; ++i) {
            if(net[i] >= 0) {
                cout << "run from i to end" << endl;
                int curr = 0;
                bool good = true;
                for (int j = i; j < n; ++j) {
                    curr += net[j];
                    if(curr < 0) {good = false; break;}
                }
                if (!good) continue;
                cout << "run from start to i" << endl;
                for(int j = 0; j < i; j++) {
                    curr += net[j];
                    if(curr < 0) {good = false; break;}
                }
                if (good || curr == 0) return i;
            }
        }
        return -1;
    }
};
