#include <bits/stdc++.h>

#define MAX 0xfffffff

using namespace std;

int graph[101][101];

int main(int argc, char const *argv[])
{
	int n, m;
	cin >> n >> m;
	
	fill(&graph[0][0], &graph[101][101], MAX);

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

	for(int i = 1; i <= n; i++) {
		for(int j =1; j <= n; j++) {
			if(graph[i][j] == MAX) cout << 0 << ' ';
			else cout << graph[i][j] << ' ';
		}
		cout << '\n';

	}
	return 0;
}
