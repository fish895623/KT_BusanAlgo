#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cassert>
#include <map>

using namespace std;

#define PLAYER 11

int max_ = 0;
int player[PLAYER][PLAYER];

void bt(vector<int> picked, bool isValid[], int toPick)
{   
    if(toPick >= PLAYER)
    {
        if(count(isValid, isValid + PLAYER, false) > 0) return;
        int sum = accumulate(picked.begin(), picked.end(), 0);
        if(max_ < sum) max_ = sum;
        return ;
    }
    for(int i = 0; i < PLAYER; i++) {
        if(player[toPick][i] == 0) continue;
        if(isValid[i]) continue;

        picked.push_back(player[toPick][i]);
        isValid[i] = true;

        bt(picked, isValid, toPick + 1);

        isValid[i] = false;
        picked.pop_back();
    }
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int test;
    cin >> test;
    for(int i = 0; i < test; i++) {
        for(int i = 0; i < PLAYER; i++)
            for(int j = 0; j < PLAYER; j++)
                cin >> player[i][j];
        
        bool isValid[PLAYER] = {false};
        vector<int> picked;

        bt(picked, isValid, 0);
        cout <<max_ << '\n';
        max_ = 0;

    }
    return 0;
}
