#include<iostream>
#include<vector>
#include<math.h>
using namespace std;

int d[5001];
int s[5001];


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	
	int n, k, power;
	cin >> n >> k;

	for (int i = 1; i <= n; i++) {
		cin >> s[i];
	}

	d[1] = true;
	for (int i = 2; i <= n; i++) {
		for (int j = 1; j < i; j++) {
			if (!d[j]) continue;
			power = (i-j) * (1 + abs(s[j] - s[i]));
			if (power <= k) {
				d[i] = true;
				break;
			}
		}
	}
	
	if (d[n]) cout << "YES";
	else cout << "NO";
}