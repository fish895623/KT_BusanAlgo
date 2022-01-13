#include<iostream>
using namespace std;

int main() {

	int s, sum = 0, cnt = 0;
	cin >> s;

	while (1) {
		cnt++;
		sum += cnt;
		if (sum > s) {
			cnt--;
			break;
		}
	}

	cout << cnt;
}