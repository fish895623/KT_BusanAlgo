#include<iostream>
using namespace std;

void prime(int n) {
	for (int i = 2; i <= n; i++) {
		while (n % i == 0) {
			n /= i;
			cout << i << '\n';
		}
	}
}

int main() {
	int n;
	cin >> n;

	prime(n);
}