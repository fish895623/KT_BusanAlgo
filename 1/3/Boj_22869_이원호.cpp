#include <bits/stdc++.h>

using namespace std;

int coin[101];
int dp[100'001];

#define MAX 987654321

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	cout.tie(nullptr);

	int n, k;
    cin >> n >> k;
    
    for(int i = 0; i <= k; i++) dp[i] = MAX;

    for(int i = 0; i < n; i++) {
        cin >> coin[i];
        dp[coin[i]] = 1;
    }
    for(int i = 1; i<=k; i++) {
        vector<int> valid;

        for(int j = 0; j < n; j++)
            if(i - coin[j] > 0) valid.push_back(dp[i - coin[j]]);
        if(valid.empty()) continue;
        int minimum = *min_element(valid.begin(), valid.end());
        minimum = minimum == MAX ? MAX : minimum + 1;
        dp[i] = min(dp[i], minimum);
    }
    if (dp[k] == MAX) cout << -1;
    else cout << dp[k];
    return 0;
}
