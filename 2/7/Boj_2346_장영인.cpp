#include<iostream>
#include<algorithm>
#include<deque>
#include<vector>
using namespace std;

int main() {
	int n, b;
	deque<pair<int, int>>q;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> b;
		q.push_back({b,i+1});
	}

	while (1) {

		int temp = q.front().first;
		int idx = q.front().second;
		q.pop_front();

		cout << idx << ' ';

		if (q.size() == 0) 
			break;

		if (temp > 0) {
			for (int i = 0; i < temp - 1; i++) {
				pair<int, int>p = q.front();
				q.pop_front();
				q.push_back(p);
			}
		}

		if (temp < 0) {
			for (int i = 0; i <abs(temp); i++) {
				pair<int, int>p = q.back();
				q.pop_back();
				q.push_front(p);
			}
		}
	}

}