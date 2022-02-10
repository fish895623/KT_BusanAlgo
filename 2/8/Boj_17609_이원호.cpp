#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int isPalindrome(string str)
{
    int size = str.length();
    string strR = str;
    reverse(strR.begin(), strR.end());
    if(str == strR) return 0;
    else
    {
        int idx = 0;
        string tmp_str = str;
        string tmp_strR = strR;

        for(; idx < size; idx++)
            if(str[idx] != strR[idx]) 
                break;
                
        str.erase(str.begin() + idx, str.begin() + idx + 1);
        strR.erase(strR.begin() + size-idx-1, strR.begin()+size-idx);
        tmp_str.erase(tmp_str.begin() + size-idx-1, tmp_str.begin()+size-idx);
        tmp_strR.erase(tmp_strR.begin() + idx, tmp_strR.begin() + idx + 1);   

        if(str == strR || tmp_str == tmp_strR)
            return 1;
        return 2;
    }
    return 0;
}

int main(int argc, char const *argv[])
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    while(n--)
    {
        string str;
        cin >> str;
        cout << isPalindrome(str) << '\n';
    }
    return 0;
}