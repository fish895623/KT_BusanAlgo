#include <iostream>
#include <regex>

using namespace std;

int main(int argc, char const *argv[]) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  int n;
  cin >> n;

  string pattern;
  cin >> pattern;

  pattern = regex_replace(pattern, regex("\\*"), "[\\w]{0,}");
  regex re(pattern);

  while (n--) {
    string target;
    cin >> target;
    if (regex_match(target, re))
      cout << "DA\n";
    else
      cout << "NE\n";
  }
  return 0;
}