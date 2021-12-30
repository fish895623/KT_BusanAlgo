#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int solution(vector<int>&rope) {
	int max = 0;
	sort(rope.begin(), rope.end());

	for (int i = 0;i < rope.size();i++) {
		int w = rope[i] * (rope.size() - i);
		if (max < w) max = w;
	}
	return max;
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n;
	vector<int>rope;

	cin >> n;
	for (int i = 0,r=0;i < n;i++) {
		cin >> r;
		rope.push_back(r);
	}

	cout<<solution(rope)<<'\n';
} 