#include<iostream>
#include<string>
using namespace std;

int main() {
	string s;
	int ans = 0, sum = 0;
	int open = 0, close = 0;

	cin >> s;

	for (int i = 0; i < s.size(); i++) {
		if (s[i] == '(') {
			sum++;
			open++;
		}
		else {
			sum--;
			close++;
		}

		if (sum <= 1)
			open = 0;
		if (sum == -1) {
			ans = close;
			break;
		}
	}

	if (sum >= 0) 
		ans = open;

	cout << ans;
}