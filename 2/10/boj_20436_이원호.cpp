#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

map<char, pair<int, int>> loc;

bool isVowel(char ch)
{
    string vowel = "yuiophjklbnm";
    auto f = find(vowel.begin(), vowel.end(), ch);
    if (f == vowel.end())
        return false;
    return true;
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    loc.insert({'q', {0, 0}});
    loc.insert({'w', {0, 1}});
    loc.insert({'e', {0, 2}});
    loc.insert({'r', {0, 3}});
    loc.insert({'t', {0, 4}});
    loc.insert({'y', {0, 5}});
    loc.insert({'u', {0, 6}});
    loc.insert({'i', {0, 7}});
    loc.insert({'o', {0, 8}});
    loc.insert({'p', {0, 9}});
    loc.insert({'a', {1, 0}});
    loc.insert({'s', {1, 1}});
    loc.insert({'d', {1, 2}});
    loc.insert({'f', {1, 3}});
    loc.insert({'g', {1, 4}});
    loc.insert({'h', {1, 5}});
    loc.insert({'j', {1, 6}});
    loc.insert({'k', {1, 7}});
    loc.insert({'l', {1, 8}});
    loc.insert({'z', {2, 0}});
    loc.insert({'x', {2, 1}});
    loc.insert({'c', {2, 2}});
    loc.insert({'v', {2, 3}});
    loc.insert({'b', {2, 4}});
    loc.insert({'n', {2, 5}});
    loc.insert({'m', {2, 6}});

    char left, right;
    string target;
    int cnt = 0;

    cin >> left >> right;
    cin >> target;

    for (auto ch : target)
    {
        pair<int, int> targetCurr = loc[ch];
        pair<int, int> curr;
        
        // 모음
        if (isVowel(ch))
        {
            curr = loc[right];
            right = ch;
        }
        // 자음
        else
        {
            curr = loc[left];
            left = ch;
        }
        
        int ty = targetCurr.first;
        int tx = targetCurr.second;
        int y = curr.first;
        int x = curr.second;
        
        cnt += abs(ty-y) + abs(tx-x) + 1;
    }
    cout << cnt;
    return 0;
}