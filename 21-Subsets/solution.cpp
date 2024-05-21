#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        long long n = pow(2, nums.size());
        vector<vector<int>> res(n);
        vector<int> arr;

        for (long long i = 0; i < n; i++) {
            arr.clear();
            for (long long j = 0; j < nums.size(); j++) {
                if ((i & (1 << j)) > 0) arr.push_back(nums[j]);
            }
            res[i] = arr;
        }

        return res;
    }
};