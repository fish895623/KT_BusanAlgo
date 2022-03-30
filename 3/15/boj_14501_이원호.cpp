#include <bits/stdc++.h>

using namespace std;

#define MAX 16

int cost[MAX];
int day[MAX];
int dp[MAX];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    for(int i = 1; i<= n; i++) {
        cin >> day[i] >> cost[i];
    }

    for(int i = n; i > 0; i--) {
        if(i + day[i] > n + 1) {
            dp[i] = dp[i+1];
            continue;
        }
        dp[i] = max(dp[i + 1], cost[i] + dp[i + day[i]]);
    }
    cout << dp[1];
    return 0;
}
