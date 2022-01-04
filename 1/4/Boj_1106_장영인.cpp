#include<iostream>
#include<algorithm>
#include<vector>
#define INF 9999999
using namespace std;

int dp[100001];
vector<pair<int, int>>v;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int c, n, a, b;
	cin >> c >> n;

	fill(dp, dp + 100001, INF);

	for (int i = 1; i <= n; i++) {
		cin >> a >> b;
		v.push_back({ b,a });
	}

	dp[0] = 0;
	for (int i = 0; i <v.size(); i++) {
		for (int j = v[i].first; j < c+101; j++) {
			dp[j] = min(dp[j], dp[j - v[i].first] + v[i].second);
		}
	}

	                       
	int ans =  INF;
	for (int i = c; i < c + 101; i++) {
		ans = min(ans, dp[i]);
	}
	cout << ans;
}