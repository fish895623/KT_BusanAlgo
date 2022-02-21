#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int n, m, ans = 1000000;
vector<int>card;

void solution(int sum,int cnt,vector<int>c) {
	if (sum > m) 
		return;

	if (cnt == 3) {
		if (abs(sum - m) < abs(ans - m))
			ans = sum;
		return;
	}
	
	for (int i = 0; i < card.size(); i++) {
		if (!c[i]) {
			c[i] = true;
			sum += card[i];
			solution(sum, cnt + 1, c);
			sum -= card[i];
			c[i] = false;
		}
	}
}

int main() {

	int c;
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> c;
		card.push_back(c);
	}

	solution(0,0,vector<int>(card.size(),0));

	cout << ans;
}