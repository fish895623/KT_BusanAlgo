#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long s;
    cin >> s;
    long long n = 1;
    long long target = 2 * s;
    while(n * (n + 1) <= target) {
        n += 1;
    }
    cout << n - 1;
	return 0;
}
