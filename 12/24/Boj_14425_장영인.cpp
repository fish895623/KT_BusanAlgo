#include<iostream>
#include<unordered_map>
#include<string>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(nullptr), cout.tie(nullptr);
    
	int n, m, cnt=0;
	string str;
	unordered_map<string, int>um;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> str;
		um[str];
	}

	for (int i = 0; i < m; i++) {
		cin >> str;
		if (um.find(str) != um.end()) cnt++;
	}

	cout << cnt;
}