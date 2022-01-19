#include <bits/stdc++.h>

using namespace std;

#define MAX 0xfffffff

int graph[1001][1001];

int main(int argc, char const *argv[])
{
	int n, m, x;
	cin >> n >> m >> x;
	
	for(int i = 1; i <= n; i++) for(int j = 1; j <= n; j++) graph[i][j] = MAX;
	for(int i = 1; i <= n; i++) graph[i][i] = 0;

	while(m--)
	{
		int s, e, c;
		cin >> s >> e >> c;
		if(graph[s][e] > c) graph[s][e] = c;
	}

	for(int k = 1; k <= n; k++) {
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				if(graph[i][k] + graph[k][j] < graph[i][j])
					graph[i][j] = graph[i][k] + graph[k][j];
			}
		}
	}
	int maxTime = 0;
	
	for(int i = 1; i <= n; i++) {
		if(i != x && graph[i][x] < MAX && graph[x][i] < MAX)
			maxTime = max(maxTime, graph[i][x] + graph[x][i]);
	}
	cout << maxTime << '\n';
	return 0;
}
