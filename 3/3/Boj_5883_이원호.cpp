#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

vector<int> arr(1'001);
vector<int> uni;

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  for (int i = 0; i < n; i++) cin >> arr[i];

  copy(arr.begin(), arr.begin() + n, back_inserter(uni));
  sort(uni.begin(), uni.end());
  uni.erase(unique(uni.begin(), uni.end()), uni.end());

  int ans = 0;

  for (auto ret : uni) {
    int cnt = 1;
    int idx = 0;

    while (arr[idx] == ret) idx++;
    int front = arr[idx];

    for (idx = idx + 1; idx < n; idx++) {
      if (arr[idx] == ret) continue;

      if (front == arr[idx]) {
        cnt++;
      } else if (front != arr[idx]) {
        front = arr[idx];
        ans = max(ans, cnt);
        cnt = 1;
      }
    }
    ans = max(ans, cnt);
  }
  cout << ans;
}