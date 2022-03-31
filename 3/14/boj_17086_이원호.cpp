#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const int dy[] = {1, 1, 1, 0, -1, -1, -1, 0};
const int dx[] = {1, 0, -1, -1, -1, 0, 1, 1};

int maps[51][51];
vector<vector<int>> visited(51, vector<int>(51, -1));

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  queue<pair<int, int>> que;

  int n, m;
  cin >> n >> m;
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> maps[i][j];
      if (maps[i][j] == 1) {
        que.push({i, j});
        visited[i][j] = 0;
      }
    }

  int ans = 0;

  while (!que.empty()) {
    auto curr = que.front();
    int y, x;

    tie(y, x) = curr;
    que.pop();

    for (int dir = 0; dir < 8; dir++) {
      int ay = y + dy[dir];
      int ax = x + dx[dir];

      if (ay < 0 || ax < 0 || ay >= n || ax >= m) continue;
      if (visited[ay][ax] >= 0) {
        continue;
      }
      visited[ay][ax] = visited[y][x] + 1;
      que.push({ay, ax});
      ans = max(ans, visited[ay][ax]);
    }
  }
  cout << ans;
  return 0;
}
