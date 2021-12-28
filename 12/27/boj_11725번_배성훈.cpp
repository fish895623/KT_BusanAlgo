#include <iostream>
#include <queue>
#include <vector>

using namespace std;

queue<int> que;
vector<int> vec[100001];
int par[100001];

void BFS() {
  while (!que.empty()) {
    int cur = que.front();
    que.pop();
    for (int i = 0; i < vec[cur].size(); i++) {
      int next = vec[cur][i];
      if (par[cur] == next)
        continue;
      que.push(next);
      par[next] = cur;
    }
  }
}

int main() {
  int N;
  cin >> N;

  for (int i = 0; i < N; i++) {
    int a1, a2;
    cin >> a1 >> a2;

    vec[a1].push_back(a2);
    vec[a2].push_back(a1);
  }
  que.push(1);
  for (int i = 0; i <= N; i++) {
    printf("%d\n", par[i]);
  }
  return 0;
}
