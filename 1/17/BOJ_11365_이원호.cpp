#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	

	while(true)
	{
		string s;
		getline(cin, s);
		if(s == "END") break;
		reverse(s.begin(), s.end());
		cout << s << '\n';
	}

	return 0;
}
