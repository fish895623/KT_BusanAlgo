#include <algorithm>
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MAX = 21;
int arr[MAX];
vector<bool> isNum(2'000'001);
vector<int> picked;

void bt(int toPick, int pick) {
  int ret = 0;
  
  for(auto p : picked) {
    ret += arr[p];
  }
  
  isNum[ret] = true;

  if(toPick == pick) {
    return;
  }

  int next = picked.empty() ? 0 : picked.back() + 1;
  for(int i = next; i < toPick; i++) {
    picked.push_back(i);
    bt(toPick, pick+1);
    picked.pop_back();
  }
}

int main(int argc, char const* argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;
  for(int i = 0; i < n; i++) cin >> arr[i];
  sort(arr, arr + n);
  bt(n, 0);
  
  int idx = 1;
  while(true) {
    if(!isNum[idx]) break;
    idx++;
  }
  cout << idx;
  return 0;
}