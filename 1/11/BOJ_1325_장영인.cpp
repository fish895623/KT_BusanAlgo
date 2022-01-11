#include<iostream>
#include<vector>
#include<queue>
#include<cstring>
using namespace std;

int n, m,cnt=0;
vector<int>c[10001];
int v[10001];
int pos[10001];

void dfs(int x) {

	v[x] = true;

	for (int i = 0; i < c[x].size(); i++) {
		int y = c[x][i];
		if (!v[y]) {
			cnt++;
			dfs(y);
		}
	}
}

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int a, b,temp=0;

	cin >> n >> m;

	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		c[b].push_back(a);
	}
	
	for (int i = 1; i <= n; i++) {
		cnt = 0;
		memset(v, 0,sizeof(v));
        
		dfs(i);
        if(temp<cnt)
            temp=cnt;
		pos[i] = cnt;

	}

	for (int i = 1; i <= n; i++) {
		if (pos[i] == temp)
			cout << i<<' ';
	}
}