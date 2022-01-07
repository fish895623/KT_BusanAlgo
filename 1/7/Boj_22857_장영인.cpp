#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, k, idx=0, ans = 0;
	int arr[50001];
	queue<int>odd;

	cin >> n >> k;
	
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}

	for (int i = 1; i <= n; i++) {
		if (arr[i] % 2 == 1)
			odd.push(i);
		if (odd.size() > k) {
			idx = odd.front();
			odd.pop();
		}
		int len = i - idx - odd.size();
		ans = max(ans,len);
	}

	cout << ans;
}