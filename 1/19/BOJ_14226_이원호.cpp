#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cassert>
#include <map>
#include <queue>

using namespace std;

int graph[1001][1001];

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    queue<pair<int, int>> que;
    que.push({1,0});

    while(!que.empty())
    {
        pair<int, int> curr = que.front(); que.pop();
        
        int node = curr.first;
        int clip = curr.second;
        // 삭제
        if(node - 1 > 1 && graph[node-1][clip] == 0)
        {
            graph[node-1][clip] = graph[node][clip] + 1;
            que.push({node-1, clip});
        }
        // 복사
        if(graph[node][node] == 0)
        {
            graph[node][node] = graph[node][clip] + 1;
            que.push({node, node});
        }
        // 붙여넣기
        if(node + clip <= n && graph[node+clip][clip] == 0)
        {
            graph[node + clip][clip] = graph[node][clip] + 1;
            que.push({node + clip, clip});
        }
    }
    int ret = 0xfffffff;
    for(int i = 1; i <= n; i++)
        if(graph[n][i] != 0 && ret > graph[n][i])
            ret = graph[n][i];
    cout << ret;
    return 0;
}
