class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto cmp = [](const vector<int>& a, const vector<int>& b) { 
            double distanceA = sqrt(pow(a[0], 2) + pow(a[1], 2));
            double distanceB = sqrt(pow(b[0], 2) + pow(b[1], 2));
            return distanceA > distanceB;
        };
        std::priority_queue<vector<int>, std::vector<vector<int>>, decltype(cmp)> mpq(cmp);
        for (vector<int> point : points) {
            mpq.push(point);
        }
        vector<vector<int>> vv;
        while(k >= 1){
            vv.push_back(mpq.top());
            mpq.pop();
            k--;
        }
        return vv;
    }
};
