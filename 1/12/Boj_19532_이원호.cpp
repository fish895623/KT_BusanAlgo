#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
	int a, b, c, d, e, f;
	cin >> a >> b >> c >> d >> e >> f;
	int div = a * e - b * d;
	int x = (c * e - b * f) / div;
	int y = (-c * d + a * f) / div;
	cout << x << ' ' << y;
	return 0;
}
