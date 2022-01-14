#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <numeric>
#include <cassert>
#include <map>

using namespace std;

int max_ = 0;
int player[11][11];

void bt(vector<int> picked, bool isValid[], int toPick)
{   
    if(toPick >= 11)
    {
        if(count(isValid, isValid + 11, false) > 0) return;
        int sum = accumulate(picked.begin(), picked.end(), 0);
        if(max_ < sum) max_ = sum;
        return ;
    }
    for(int i = 0; i < 11; i++) {
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
        for(int i = 0; i < 11; i++)
            for(int j = 0; j < 11; j++)
                cin >> player[i][j];
        
        bool isValid[11] = {false};
        vector<int> picked;

        bt(picked, isValid, 0);
        cout <<max_ << '\n';
        max_ = 0;

    }
    return 0;
}
