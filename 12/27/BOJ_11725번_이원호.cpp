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

    queue<pair<int, int>> que;

    int n;
    int root[100001] = {};    
    map<int, vector<int>> graph;
    cin >> n;
    
    for(int i = 0; i < n - 1; i++) {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    // init
    for(auto iter : graph[1]) {
        que.push({1, iter});
    }
    
    while(!que.empty()) {
        pair<int ,int> node = que.front();
        que.pop();

        int pre_node = node.first;
        int nxt_node = node.second;

        if(root[nxt_node] == 0) {
            for(auto iter : graph[nxt_node]) {
                que.push({nxt_node, iter});
            }
            root[nxt_node] = pre_node;
        }
    }
    for(int i = 2; i <= n; i++) cout << root[i] << '\n';

    return 0;
}



