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

using namespace std;


int main(int argc, char const *argv[])
{
    
    map<string, int> tree;
    string s;
    int cnt = 0;
    
    while(getline(cin, s))
    {
        cnt++;
        auto item = tree.find(s);
        if(item != tree.end()) {
            item->second += 1;
        }
        else {
            tree.insert({s, 1});
        }
    }
    for(auto t : tree)
    {
        cout << t.first << ' ';
        printf("%.4f\n", t.second/double(cnt) * 100);
    }
    return 0;
}