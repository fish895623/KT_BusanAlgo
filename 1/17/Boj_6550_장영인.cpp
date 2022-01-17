#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string s,t;
	int cnt = 0;

	while (!(cin >> s >> t).eof()) {
		cnt = 0;
		for (int i = 0; i < t.length(); i++) {
			if (s[cnt] == t[i]) cnt++;
			if (cnt == s.length()) break;
		}

		if (cnt == s.length()) cout << "Yes"<<'\n';
		else cout<<"No"<<'\n';
	}
}