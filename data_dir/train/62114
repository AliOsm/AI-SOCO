#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, OO = 2e9 + 9;

int main() {
  debug();
  int n, x, y, cnt = 0;
  string str;
  cin >> n >> x >> y;
  cin >> str;
  reverse(all(str));
  if (str[y] == '0')
    ++cnt;
  for (int i = 0; i < x; ++i) {
    if (i == y)
      continue;
    if (str[i] == '1')
      ++cnt;
  }
  cout << cnt;
}
