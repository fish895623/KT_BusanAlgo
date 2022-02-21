#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main() {
	vector<pair<int, int>>key[100];
	string str;
	char left, right;
	int lx, ly,rx,ry, sum = 0;

	char arr1[10] = { 'q','w','e','r','t','y','u','i','o','p' };
	char arr2[9] = { 'a','s','d','f','g','h','j','k','l' };
	char arr3[7] = { 'z','x','c','v','b','n','m' };
	
	for (int i = 0; i < sizeof(arr1); i++) {
		key[arr1[i] - '0'].push_back({ i,0 });
	}
	for (int i = 0; i < sizeof(arr2); i++) {
		key[arr2[i] - '0'].push_back({ i,1 });
	}
	for (int i = 0; i < sizeof(arr3); i++) {
		key[arr3[i] - '0'].push_back({ i,2 });
	}

	cin >> left>>right;
	cin >> str;
	
	for (int i = 0; i < str.size(); i++) {
		char c = str[i];
		int cx = key[c - '0'].front().first;
		int cy = key[c - '0'].front().second;

		if (cx>=5||(cx==4&&cy==2)) {
			rx = key[right - '0'].front().first;
			ry = key[right - '0'].front().second;
			right = c;
			sum += abs(cx - rx) + abs(cy - ry)+1;
		}
		else {
			lx = key[left - '0'].front().first;
			ly = key[left - '0'].front().second;
			left = c;
			sum += abs(cx - lx) + abs(cy - ly)+1;
		}
	}
	cout << sum;
}