#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(void) {
	cin.tie(0);
	cin.sync_with_stdio(0);

	int n, num;
	queue<int> q;
	string str;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> str;

		if (str == "push") {
			cin >> num;
			q.push(num);
		}
		else if (str == "pop") {
			if (q.size() == 0) 
				std::cout << "-1\n";
			else {
				num = q.front();
				q.pop();
				cout << num << "\n";
			}
		}
		else if (str == "empty") {
			cout << q.empty() << "\n";
		}
		else if (str == "size") {
			cout << q.size() << "\n";
		}
		else if (str == "front") {
			if (q.size() == 0)
				std::cout << "-1\n";
			else cout << q.front() << "\n";
		}
		else if (str == "back") {
			if (q.size() == 0)
				std::cout << "-1\n";
			else cout << q.back() << "\n";
		}
	}
	return 0;
}