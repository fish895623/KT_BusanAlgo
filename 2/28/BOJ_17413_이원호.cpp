#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

string ans = "";

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string str;
  getline(cin, str);

  bool isBracket = false;
  string tmp = "";

  for (auto ch : str) {
    if (ch == '<') {
      if (tmp.size() > 0) {
        reverse(tmp.begin(), tmp.end());
        ans += tmp;
        tmp.clear();
      }
      tmp += ch;
      isBracket = true;
    } else if (ch == '>') {
      tmp += ch;
      ans += tmp;
      isBracket = false;
      tmp.clear();
    } else if (ch == ' ') {
      if (isBracket) {
        tmp += ch;
      } else {
        reverse(tmp.begin(), tmp.end());
        tmp += " ";
        ans += tmp;
        tmp.clear();
      }
    } else {
      tmp += ch;
    }
  }
  if (int(tmp.size()) > 0) {
    reverse(tmp.begin(), tmp.end());
    ans += tmp;
  }
  cout << ans;
  return 0;
}