#include<iostream>
#include<queue>
#define MAX 1001
using namespace std;

int n, loc = 0;
int pre[MAX], in[MAX];

void post(int left, int right) {
	if (left >= right) return;

	int idx = 0;
	for (int i = left; i < right; i++) {
		if (pre[loc] == in[i]) {
			loc++;
			idx = i;
			break;
		}
	}

	post(left,idx);
	post(idx + 1, right);
	cout << in[idx]<<' ';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int t;
	cin >> t;

	for (int i = 0; i < t; i++) {
		loc = 0;
		cin >> n;

		for (int i = 0; i < n; i++) {
			cin >> pre[i];
		}
		for (int i = 0; i < n; i++) {
			cin >> in[i];
		}
		post(0, n);
		cout << '\n';

	}
}