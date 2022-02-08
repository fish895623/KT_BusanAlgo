#include<iostream>
#include<string>
#include<queue>
using namespace std;

void valid(string s) {
	int start = 0;
	int end = s.size() - 1;
	int diff = 0, ans = 0;
	queue<pair<int, int>>q;

	while (start <= end && diff<3) {

		if (q.size()==2||diff==2&&!q.empty()) {
			start = q.front().first;
			end = q.front().second;
			q.pop();
		}
		if (s[start] == s[end]) {
			start++;
			end--;
		}
		else {
			diff++;
			if (diff==1) {
				q.push({ start + 1,end });
				q.push({ start,end - 1 });
			}
		}
	}

	if (diff > 2)
		ans = 2;
	else if (diff > 0)
		ans = 1;

	cout << ans<<'\n';
}

int main() {
	int t;
	string s;

	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> s;
		valid(s);
	}

}