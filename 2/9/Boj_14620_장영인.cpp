#include<iostream>
#include<algorithm>
#include<limits.h>
using namespace std;


const int dy[4] = { 1,-1,0,0 };
const int dx[4] = { 0,0,1,-1 };

int n, result=INT_MAX;
int map[10][10];
int visit[10][10];

bool check(int y, int x) {
	if (visit[y][x]) return true;
	for (int i = 0; i < 4; i++) {
		int cy = y + dy[i];
		int cx = x + dx[i];
		if (visit[cy][cx]) return true;
	}
	return false;
}

int use(int y, int x) {
	int cost = 0;
	cost += map[y][x];
	visit[y][x] = true;
	for (int i = 0; i < 4; i++) {
		int cy = y + dy[i];
		int cx = x + dx[i];
		visit[cy][cx] = true;
		cost += map[cy][cx];
	}
	return cost;
}

void not_use(int y, int x) {
    visit[y][x] = false;
	for (int i = 0; i < 4; i++) {
		int cy = y + dy[i];
		int cx = x + dx[i];
		visit[cy][cx] = false;
	}
}

void solution(int depth,int temp) {
	if (depth == 3) {
		result = min(result, temp);
		return;
	}

	for (int i = 1; i < n - 1; i++) {
		for (int j = 1; j < n - 1; j++) {
			if (check(i, j)) continue;
			int c = use(i, j);
			solution(depth + 1, temp+c);
			not_use(i, j);
		}
	}
}

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> map[i][j];
		}
	}

	solution(0, 0);
	cout << result;
}