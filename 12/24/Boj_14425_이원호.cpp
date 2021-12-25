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

using namespace std;


int main(int argc, char const *argv[])
{
    set<string> set_;
    string s;
    int n, m;
    cin >> n >> m;
    int ans = 0;
    while(n--) {
        cin >> s;
        set_.insert(s);
    }
    while(m--) {
        cin >> s;
        auto item = set_.find(s);
        if(item != set_.end()) ans += 1;
    }
    cout << ans;
    return 0;
}