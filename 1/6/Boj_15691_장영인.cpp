#include<iostream>
#include<deque>
#include<vector>
#include<algorithm>
using namespace std;

int p[3000001];
int v[3001];
deque<int>dq;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, d, k, c;
	int cnt = 0, ans = 0;

	cin >> n >> d >> k >> c;

	for (int i = 0; i < n; i++) {
		cin >> p[i];
	}

	for (int i = 0; i < k; i++) {
		dq.push_back(p[i]);
		if (v[p[i]] == 0) {
			cnt++;
		}
		v[p[i]]++;
		ans = max(ans, cnt);
	}

	for (int i = 0; i < n -1; i++) {
		dq.pop_front();
		v[p[i]]--;
		if (v[p[i]] == 0) {
			cnt--;
		}

		dq.push_back(p[(i + k) % n]);

		if (v[p[(i + k) % n]] == 0) {
			cnt++;
		}
		v[p[(i + k) % n]]++;

		if (!v[c])
			ans = max(ans, cnt + 1);
		else 
			ans = max(ans, cnt);
		
	}

	cout << ans;
	return 0;
}