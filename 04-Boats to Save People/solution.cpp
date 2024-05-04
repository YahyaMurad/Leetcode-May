#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin(), people.end());

        int l = 0, r = people.size() - 1;
        int res = 0;
        while (l < r) {
            if (people[l] + people[r] <= limit) {
                l++;
            }
            r--;
            res++;

        }

        if (l == r) res++;

        return res;
    }
};

int main() {
    Solution sol;
    vector<int> people = {1, 2, 3, 3, 3, 3, 3, 5};
    int limit = 7;

    cout << sol.numRescueBoats(people, limit) << "\n";
}