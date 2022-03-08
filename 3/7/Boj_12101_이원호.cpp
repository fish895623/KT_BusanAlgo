#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int cnt = 0;
vector<int> picked;

void func(int n, int k, int sum) {
  if (n == sum) {
    cnt++;
    if (k == cnt) {
      for (int i = 0; i < int(picked.size()); i++) {
        cout << picked[i];
        if (i < int(picked.size()) - 1) cout << '+';
      }
    }
    return;
  }
  for (auto ret : {1, 2, 3}) {
    if (sum + ret > n) continue;
    picked.push_back(ret);
    func(n, k, sum + ret);
    picked.pop_back();
  }
}

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n, k;
  cin >> n >> k;
  func(n, k, 0);
  if (cnt < k) cout << -1;
  return 0;
}
