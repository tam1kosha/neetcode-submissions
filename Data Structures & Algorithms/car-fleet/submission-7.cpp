class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int count = 1;
        int n = position.size();
        vector<pair<int, int>> cars(n);
        for (int i = 0; i < n; ++i) {
            cars[i] = {position[i], speed[i]};
        }
        sort(cars.begin(), cars.end(), [](const pair<int, int>& a, const pair<int, int>& b){
            return a.first < b.first;
        });
        vector<double> travel_time(n);
        for (int i = 0; i < n; ++i) {
            travel_time[i] = static_cast<double>((target - (cars[i].first))) / cars[i].second;
        }

        double current = travel_time[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            if (travel_time[i] > current) {
                current = travel_time[i];
                count++;
            } 
        }
        return count;
    }
};
