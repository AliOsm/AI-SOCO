#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef long double Double;

string vowels = "aeiou";

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  string s;
  cin >> s;

  int cn = 0;
  set<char> st;

  for (char c : s) {
    if (vowels.find(c) != string::npos) {
      cn = 0;
      st.clear();
    } else {
      ++cn;
      st.insert(c);
    }

    if (cn >= 3 && st.size() > 1) {
      cout << ' ';
      cn = 1;
      st.clear();
      st.insert(c);
    }

    cout << c;
  }

}

