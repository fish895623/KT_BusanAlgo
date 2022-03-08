#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

unordered_map<string, string> chatLog;
set<string> ans;

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string s, e, q;
  string log;
  cin >> s >> e >> q;

  while (getline(cin, log)) {
    auto pos = log.find(' ');

    string time = log.substr(0, pos);
    string name = log.substr(pos + 1);

    if (chatLog.find(name) != chatLog.end()) {
      string logTime = chatLog.at(name);
      if (logTime <= s && time >= e && time <= q) ans.insert(name);
    } else
      chatLog.insert({name, time});
  }
  cout << int(ans.size());
  return 0;
}