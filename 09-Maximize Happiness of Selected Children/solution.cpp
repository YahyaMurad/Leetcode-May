#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>());
        
        long long res = 0;
        int counter = 0;

        for (int i = 0; i < min(k, static_cast<int>(happiness.size())); ++i) {
            res += max(0, happiness[i] - counter);
            ++counter;
        }
        return res;
    }
};