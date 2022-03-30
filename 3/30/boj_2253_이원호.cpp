#include <bits/stdc++.h>

using namespace std;

const int INF = 0xffffff;
const int MAX = 200;

vector<vector<int>> dp(10'001, vector<int>(MAX, INF));
int arr[10'001];

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  for (int i = 0; i < m; i++) {
    int x;
    cin >> x;
    arr[x] = 1;
  }

  dp[1][0] = 0;

  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < MAX; j++) {
      if (dp[i][j] == INF) continue;

      for (auto jmp : {j - 1, j, j + 1}) {
        if (jmp <= 0 || i + jmp > n || arr[i + jmp] == 1) continue;
        dp[i + jmp][jmp] = min(dp[i + jmp][jmp], dp[i][j] + 1);
      }
    }
  }
  int ans = INF;
  for (int i = 0; i < MAX; i++) ans = min(ans, dp[n][i]);
  if (ans == INF) ans = -1;
  cout << ans;
  return 0;
}
