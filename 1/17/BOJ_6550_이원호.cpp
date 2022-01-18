#include <bits/stdc++.h>

using namespace std;

bool isInString(string str, string comp)
{
	int findIdx = 0;
	bool isIn = false;

	for(int idx = 0; idx < int(comp.size()); idx++)
	{
		if(str[findIdx] == comp[idx]) findIdx += 1;
		if(findIdx == int(str.size())) {
			isIn=true;
			break;
		}
	}
	return isIn;
}

int main(int argc, char const *argv[])
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
    string s, t;
    while(!(cin >> s >> t).eof())
    {
        if(isInString(s, t)) cout << "Yes\n";
        else cout << "No\n";
    }

	return 0;
}
