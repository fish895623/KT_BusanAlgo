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
#include <string>
#include <regex>

using namespace std;

struct baseBall
{
    vector<int> num;
    int strike;
    int ball;
};

int answer = 0;
vector<baseBall> baseBallArr;


bool check(vector<int> picked)
{
    for(auto val : baseBallArr) {
        int s = 0, b = 0;
        for(int i = 0; i < picked.size(); i++) {
            if (val.num[i] == picked[i]) s++;
            else {
                if (find(picked.begin(), picked.end(), val.num[i]) != picked.end()) b++;
            }
        }
        if (val.strike != s || val.ball != b) return false;
    }
    return true;
}

void get_num(vector<int> &picked, int toPick)
{
    if(toPick == 0)
    {
        if (check(picked)) answer += 1;
        return ;
    }
    for(int i = 1; i <= 9; i++)
    {
        if(find(picked.begin(), picked.end(), i) != picked.end()) continue;
        picked.push_back(i);
        get_num(picked, toPick - 1);
        picked.pop_back();
    }
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    
    vector<int> picked;
    cin >> n;
    while(n--) {
        int num, strike, ball;
        baseBall bB;
        cin >> num >> strike >> ball;
        while(num > 0) {
            bB.num.push_back(num % 10);
            num /= 10;
        }
        reverse(bB.num.begin(), bB.num.end());
        bB.strike = strike;
        bB.ball = ball;
        baseBallArr.push_back(bB);
    }
    get_num(picked, 3);
    cout << answer;
    return 0;
}
