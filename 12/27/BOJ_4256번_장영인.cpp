#include<iostream>
#define MAX 1001
using namespace std;

int n, t, loc = 0;
int pre[MAX], in[MAX];

void post(int left, int right) {
	if (left > right)
		return;

	int idx;
	for (int i = left; i <= right; i++) {
		if (pre[loc] == in[i]) {
			idx = i;
			loc++;
			break;
		}
	}

	post(left, idx - 1);
	post(idx + 1, right);
	cout << in[idx] << ' ';
}

int main() {

	cin >> t;
	
	for (int i = 0; i < t; i++) {
		
        loc = 0;
        
        cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> pre[i];
		}
		for (int i = 0; i < n; i++) {
			cin >> in[i];
		}

		post(0,n-1);
		cout << '\n';
	}

}