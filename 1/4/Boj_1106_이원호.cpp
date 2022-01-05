#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>
#include <cmath>
#include <queue>
#include <list>
#include <stack>
#include <stdio.h>
#include <set>
#include <functional>

using namespace std;

#define MAX 987654321

int dp[1101];
vector<pair<int, int>> li;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int c, n;
    cin >> c >> n;
    for(int i = 1; i <= c + 100; i++) dp[i] = MAX;
    for(int i = 0; i < n; i++) {
        int price, customer;
        cin >> price >> customer;
        li.push_back({price, customer});
    }

    for(int i = 1; i <= c+100; i++) {
        vector<int> valid;

        for(auto val : li) {
            int price = val.first;
            int customer = val.second;
            if(i - customer < 0) continue;
            valid.push_back(dp[i - customer] + price);
        }
        if(valid.empty()) continue;

        int minimum = *min_element(valid.begin(), valid.end());

        dp[i] = dp[i] > minimum ? minimum : dp[i];

        for(int j = 1; j < i; j++) {
            if (dp[j] > dp[i]) dp[j] = dp[i];
        }
    }
    cout << dp[c];
    return 0;
}

