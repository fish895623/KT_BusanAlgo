#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int MAX = 101;

vector<bool> wall(MAX, true);

void func(int start, int end) {
  for (int i = start + 1; i <= end; i++) wall[i] = false;
}

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, m;
  cin >> n >> m;

  for (int i = 0; i <= n; i++) wall[i] = i;

  while (m--) {
    int x, y;
    cin >> x >> y;
    func(x, y);
  }
  int ans = 1;
  for (int i = 1; i <= n; i++)
    if (wall[i]) ans++;
  cout << ans - 1;
  return 0;
}