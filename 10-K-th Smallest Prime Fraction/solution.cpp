#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        vector<pair<vector<int>, double>> fractions;

        for (int i = 0; i < arr.size(); ++i) {
            for (int j = 0; j < arr.size(); ++j) {
                fractions.push_back({{arr[i], arr[j]}, static_cast<double>(arr[i]) / arr[j]});
            }
        }

        sort(fractions.begin(), fractions.end(), [](const auto& a, const auto& b) {
            return a.second < b.second;
        });

        return fractions[k - 1].first;
    }
};