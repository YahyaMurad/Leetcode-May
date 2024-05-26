#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int specialArray(vector<int>& nums) {
        int x = nums.size();
        int cnt;

        while (x != 0) {
            cnt = 0;
            for (int n : nums) {
                if (n >= x) cnt++;
            }

            if (cnt == x) return x;

            x--;
        }

        return -1;
    }
};