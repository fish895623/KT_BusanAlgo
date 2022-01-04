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

int stone[5001];
int dp[5001];

#define MAX 987654321

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);
	int n, k;
	cin >> n >> k;
	for(int i = 1; i <= n; i++) cin >> stone[i];
	for(int i = 2; i <= n; i++) dp[i] = MAX;

	for(int i = 1; i <= n; i++) {
		if (dp[i] > k) continue;
		for(int j = i + 1; j <= n; j++) {
			int cost = (j-i) * (1 + abs(stone[i] - stone[j]));
			cost = cost > k ? MAX : cost;
			dp[j] = min(dp[j], cost);
		}
	}
	if(dp[n] == MAX) cout << "NO";
	else cout << "YES";
	return 0;
}
