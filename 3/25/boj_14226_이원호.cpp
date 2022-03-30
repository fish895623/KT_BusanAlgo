#include <bits/stdc++.h>

using namespace std;

int maps[1001][1001];

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  queue<pair<int, int>> que;
  que.push({1, 0});

  while (!que.empty()) {
    int node, clip;
    tie(node, clip) = que.front();
    que.pop();

    // copy
    if (maps[node][node] == 0) {
      maps[node][node] = maps[node][clip] + 1;
      que.push({node, node});
    }
    // paste
    if ((node + clip) <= n && maps[node + clip][clip] == 0) {
      maps[node + clip][clip] = maps[node][clip] + 1;
      que.push({node + clip, clip});
    }
    // delete
    if ((node - 1) > 0 && maps[node - 1][clip] == 0) {
      maps[node - 1][clip] = maps[node][clip] + 1;
      que.push({node - 1, clip});
    }
  }

  int ans = 0xfffffff;
  for (int i = 1; i <= n; i++)
    if (maps[n][i] != 0 && ans > maps[n][i]) ans = maps[n][i];
  cout << ans;
  return 0;
}
