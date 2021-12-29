#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
#define MAX 1500001

int dp[MAX];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, p, t;
	vector<pair<int, int>>v;

	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> t >> p;
		v.push_back({t,p});
	}

	for (int i = n-1; i >= 0; i--) {
		if (n < i + v[i].first)
			dp[i] = dp[i + 1];
		else 
			dp[i] = max(dp[i + 1], dp[i + v[i].first] + v[i].second);
	}

	cout << dp[0];
}