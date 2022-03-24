#include <bits/stdc++.h>

using namespace std;

const int MAX = 101;

vector<pair<int, int>> bike(MAX), step(MAX);
int dp[MAX][100'001];

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;
  for (int i = 1; i <= n; i++)
    cin >> step[i].first >> step[i].second >> bike[i].first >> bike[i].second;

  dp[1][step[1].first] = step[1].second;
  dp[1][bike[1].first] = max(dp[1][bike[1].first], bike[1].second);

  for (int i = 2; i <= n; i++) {
    for (int j = 0; j <= k; j++) {
      if (dp[i - 1][j] == 0) continue;

      int st, sm;
      int bt, bm;

      tie(st, sm) = step[i];
      tie(bt, bm) = bike[i];

      if (j + st <= k) dp[i][j + st] = max(dp[i][j + st], dp[i - 1][j] + sm);
      if (j + bt <= k) dp[i][j + bt] = max(dp[i][j + bt], dp[i - 1][j] + bm);
    }
  }

  int ans = 0;
  for (int i = 1; i <= k; i++) ans = max(ans, dp[n][i]);
  cout << ans;
  return 0;
}
