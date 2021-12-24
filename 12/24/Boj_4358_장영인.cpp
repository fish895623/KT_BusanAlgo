#include<iostream>
#include<map>
#include<string>
using namespace std;

int main() {
	double rate, total = 0;
	string str;
	map<string, double> m;

	while (getline(cin,str)){
		m[str]++;
		total++;
	}

	cout << fixed;
	cout.precision(4);

	for (auto iter = m.begin(); iter != m.end(); iter++) {
		rate = iter->second / total * 100;
		cout << iter->first <<" "<< rate << '\n';
	}
}