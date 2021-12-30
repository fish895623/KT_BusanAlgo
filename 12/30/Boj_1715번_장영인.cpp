#include<iostream>
#include<queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);

	int n, c, sum = 0;
	priority_queue<int, vector<int>, greater<int>>card;

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> c;
		card.push(c);
	}

	while (card.size() != 1) {
		int mix = card.top(); 
		card.pop();
		mix += card.top();
		card.pop();
		card.push(mix);
		sum += mix;
	}

	cout << sum;

}