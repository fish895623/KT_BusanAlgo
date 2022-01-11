#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;

int n, m, a, b;
bool suc = false;
vector<int>c[2001];
int v[2001];

bool dfs(int x,int cnt) {

    v[x] = true;

	if (cnt == 4) {
		suc = true;
		return suc;
	}

	for (int i = 0; i < c[x].size(); i++) {
		int y = c[x][i];
		if (!v[y]) {
			dfs(y,cnt+1);
			v[y] = false;
		}
	}
	return suc;
}

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		c[a].push_back(b);
		c[b].push_back(a);
	}

	for (int i = 1; i <= n; i++) {
		suc = false;
		memset(v, 0, sizeof(v));
		if (dfs(i, 0)) break;
	}

	if (suc) cout << 1;
	else cout << 0;
}