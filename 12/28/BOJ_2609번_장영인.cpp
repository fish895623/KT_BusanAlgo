#include<iostream>
using namespace std;

int gcd(int a,int b) {
	return b == 0 ? a : gcd(b, a % b);
}

int multiple(int a,int b,int c) {
	return a * b / c;
}

int main() {
	int a, b, c, d;
	cin >> a >> b;

	c = gcd(a, b);
	d = multiple(a, b, c);

	cout << c << '\n';
	cout << d << '\n';
}