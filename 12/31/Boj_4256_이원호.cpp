#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <numeric>
#include <cmath>
#include <queue>
#include <list>
#include <stack>
#include <stdio.h>
#include <set>
#include <functional>

using namespace std;

int preOrder[1001];
int inOrder[1001];

void postOrder(int s, int e, int r) {
	for(int i = s; i < e; i++) {
		if(inOrder[i] == preOrder[r]) {
			postOrder(s, i, r + 1);
			postOrder(i + 1, e, r + 1 + i - s);
			cout << preOrder[r] << ' ';
		}
	}
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	cout.tie(nullptr);

	int t;
	cin >> t;
	while (t--) {
		int n;
		cin >> n;
		for(int i = 0; i < n; i++) cin >> preOrder[i];
		for(int i = 0; i < n; i++) cin >> inOrder[i];
		
		postOrder(0, n, 0);
		cout << "\n";
	}
    return 0;
}
