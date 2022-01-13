#include<iostream>
#include<limits.h>
#include<vector>
using namespace std;

long long solution(vector<int> v, int n) {
	long long result = 0;
	long long start = 0;
	long long end = LLONG_MAX;

	while (start <= end) {
		long long total = 0;
		long long  mid = (start + end) / 2;

		for (int i = 0; i < v.size(); i++) {
			total += v[i] / mid;
		}

		if (total < n) {
			end = mid - 1;
		}
		else {
			result = mid;
			start = mid + 1;
		}
	}
	return result;
}

int main() {

	int k, n, line;
	cin >> k >> n;

	vector<int>v;

	for (int i = 0; i < k; i++) {
		cin >> line;
		v.push_back(line);
	}

	cout << solution(v, n);
}