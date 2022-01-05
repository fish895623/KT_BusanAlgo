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

int dp[10'001];
int arr[10'001];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;

    cin >> n;
    
    for(int i = 1; i <= n; i++) cin >> arr[i];

    dp[1] = arr[1];
    dp[2] = arr[1] + arr[2];
    for(int i = 3; i <=n; i++) {
        vector<int> valid;

        valid.push_back(dp[i-3] + arr[i-1] + arr[i]);
        valid.push_back(dp[i-2] + arr[i]);
        valid.push_back(dp[i-1]);

        dp[i] = *max_element(valid.begin(), valid.end());
    }
    cout << dp[n];
    return 0;
}

