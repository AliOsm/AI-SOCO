#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
//  freopen("out.txt", "w", stdout);
#endif

  int n, m;
  cin >> n >> m;
  int both = 0;
  set<string> a;

  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    a.insert(s);
  }

  for (int i = 0; i < m; ++i) {
    string s;
    cin >> s;
    both += a.count(s);
  }

  both &= 1;

  if (n > m || both && n == m) {
    cout << "YES";
  } else {
    cout << "NO";
  }


}
