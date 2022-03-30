#include <bits/stdc++.h>

using namespace std;

const int MAX = 5001;

int height[MAX];
vector<int> cache(MAX, -1);
vector<int> maps[MAX];

int dp(int point) {
  int& ret = cache[point];
  if (ret != -1) return ret;

  ret = 1;
  for (auto nxt : maps[point]) ret = max(ret, dp(nxt) + 1);
  return ret;
}

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  for (int i = 1; i <= n; i++) cin >> height[i];

  while (m--) {
    int a, b;
    cin >> a >> b;

    if (height[a] > height[b])
      maps[b].push_back(a);
    else
      maps[a].push_back(b);
  }

  for (int point = 1; point <= n; point++) {
    cout << dp(point) << '\n';
  }
  return 0;
}
