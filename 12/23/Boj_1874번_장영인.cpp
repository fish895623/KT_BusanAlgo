#include <iostream>
#include <vector>
using namespace std;


int main(void) {
	cin.tie(0);
	cin.sync_with_stdio(0);

	int n, idx = 0;
	int seq[100001];
	vector<int>v;
	vector<char>op;

	cin >> n;

	for (int i = 0;i < n;i++)
		cin >> seq[i];

	for (int i = 1;i <= n;i++) {
		v.push_back(i);
		op.push_back('+');

		while (!v.empty() && v.back() == seq[idx]) {
			idx++;
			v.pop_back();
			op.push_back('-');
		}
	}

	if (!v.empty())
		cout << "NO" << '\n';
	else {
		for (int i = 0;i < op.size();i++)
			cout << op[i] << '\n';
	}
	return 0;
}