#include<iostream>
#include<vector>
#define MAX 100001
using namespace std;

int v[MAX];
int p[MAX];
vector<int>g[MAX];

void dfs(int x) {
	if (v[x] == true) return;
	v[x] = true;
	for (int i = 0; i < g[x].size(); i++) {
		int y = g[x][i];
		dfs(y);
		p[y] = x;
	}
}

int main() {

	int a, b, n;

	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		cin >> a >> b;
		g[a].push_back(b);
		g[b].push_back(a);
	}

	dfs(1);

	for (int i = 2; i <= n; i++) {
		cout << p[i] << '\n';
	}

}