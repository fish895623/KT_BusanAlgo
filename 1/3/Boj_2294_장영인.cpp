#include<iostream>
#define INF 99999
using namespace std;

int c[101];
int dp[10001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, k;
	cin >> n >> k;

	fill(dp, dp + 10001,INF);

	for (int i = 1; i <= n; i++) {
		cin >> c[i];
	}

	dp[0] = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = c[i]; j <= k; j++) {
			dp[j] = min(dp[j], dp[j - c[i]] + 1);
		}
	}

	if (dp[k] == INF) cout << -1;
	else cout << dp[k];
}