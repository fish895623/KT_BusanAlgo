#include<iostream>
#include<vector>
using namespace std;

long long solution(vector<long long>&dist, vector<long long>&cost) {
	long long total = 0;
    int idx = 0;
    
	total += cost[0] * dist[1];
    
	for (int i = 1;i < dist.size() - 1;i++) {
		if (cost[i] < cost[idx]) {
			total += cost[i] * dist[i + 1];
			idx = i;
		}
		else total += cost[idx] * dist[i + 1];
	}
    
	return total;
}

int main() {
	int n;
	cin >> n;

	vector<long long>dist(n, 0);
	vector<long long>cost(n, 0);

	for (int i =1;i < n ;i++) {
		cin >> dist[i];
	}
	for (int i = 0;i < n;i++) {
		cin >> cost[i];
	}

	cout<<solution(dist, cost);
}