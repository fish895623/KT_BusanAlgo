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

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	cout.tie(nullptr);

    priority_queue<int, vector<int>, greater<int>> card;
    int n;
    int cnt = 0;
    cin >> n;
    while (n--) {
        int x;
        cin >> x;
        card.push(x);
    }

    while (card.size() > 1) {
        int first = card.top();
        card.pop();
        int second = card.top();
        card.pop();

        cnt += (first + second);
        card.push(first + second);
    }
    cout << cnt;
    return 0;
}
