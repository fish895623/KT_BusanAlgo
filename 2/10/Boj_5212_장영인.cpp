#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int r, c;
char map[10][10];
int sink[10][10];

int dy[4] = { 0,0,1,-1 };
int dx[4] = { 1,-1,0,0 };

void solution() {

	for (int y = 0; y < r; y++) {
		for (int x = 0; x < c; x++) {
			if (map[y][x] == '.') 
				continue;

			int cnt = 0;

			for (int k = 0; k < 4; k++) {
				int cy = y + dy[k];
				int cx = x + dx[k];

				if (cy < 0 || cx < 0 || cy > r - 1 || cx > c - 1) {
					cnt++;
					continue;
				}

				if (map[cy][cx] == '.') cnt++;
			}

			if (cnt >= 3)
				sink[y][x] = true;
		}
	}

	int cmin = 11, cmax = -1;
	int rmin = 11, rmax = -1;

	for (int y = 0; y < r; y++) {
		for (int x = 0; x < c; x++) {
			if (!sink[y][x] && map[y][x] == 'X') {
				cmin = min(cmin, x);
				cmax = max(cmax, x);
				rmin = min(rmin, y);
				rmax = max(rmax, y);
			}
		}
	}

	for (int y = rmin; y <= rmax; y++) {
		for (int x = cmin; x <= cmax; x++) {
			if (map[y][x] == 'X' && sink[y][x])
				cout << '.';
			else cout << map[y][x];
		}
		cout << '\n';
	}
}

int main() {
	cin >> r >> c;

	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> map[i][j];
		}
	}

	solution();
}