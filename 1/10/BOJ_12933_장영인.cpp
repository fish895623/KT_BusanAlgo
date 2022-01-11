#include<iostream>
#include<vector>
#define MAX 2500
using namespace std;

int v[MAX];

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	string s;
    string cry = "quack";
	int idx = 0, cnt = 0;

	cin >> s;

	for (int i = 0; i < s.length(); i++) {
		if (s.length() % 5 != 0) 
			break;

		if (!v[i] && s[i] == 'q') {

			for (int j = i; j < s.length(); j++) {
				if (v[j]) continue;

				if (cry[idx % 5] == s[j]) {
					idx++;
					v[j] = true;
				}
			}

			if (idx==0 || idx % 5 != 0)
				break;
			else cnt++;
		}
	}


	if (cnt!=0 && idx==s.length()) 
		cout << cnt;
	else cout << -1;

 }