#include <bits/stdc++.h>
using namespace std;

const int N = 5e4;
int nxt[N];
int main() {
  string s;
  cin >> s;

  for (char c = 'A'; c <= 'Z'; ++c) {
    int lst = s.size();
    for (int i = s.size() - 1; i >= 0; --i)
      if (s[i] == c) {
        nxt[i] = lst;
        lst = i;
      }
  }

  int begin = 0;
  bool found = false;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '?') nxt[i] = s.size();
    if (nxt[i] < begin + 26) {
      begin = i + 1;
    }
    if (i - begin + 1 == 26) {
      found = true;
      break;
    }
  }

  if (!found)
    cout << -1;
  else {
    set<char> st;
    for (char c = 'A'; c <= 'Z'; ++c) st.insert(c);
    for (int i = begin; i < begin + 26; ++i) {
      if (s[i] != '?') st.erase(s[i]);
    }
    for (int i = begin; i < begin + 26; ++i) {
      if (s[i] == '?') {
        s[i] = *st.begin();
        st.erase(s[i]);
      }
    }
    for (char& c : s)
      if (c == '?') c = 'A';
    cout << s;
  }

  return 0;
}
