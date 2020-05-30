#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, M = 2e5 + 2, OO = 1e9 + 9, MOD = 1e9 + 7;

pair<int, char> tab[N];

int main() {
  fastIO
  int n, idx;
  cin >> n;
  char c;
  int l = 0, r = 0;
  for (int i = 0; i < n; ++i) {
    cin >> c >> idx;
    if(c == 'L') {
      ++l;
      tab[idx] = {l, 'L'};
    } else if(c == 'R') {
      ++r;
      tab[idx] = {r, 'R'};
    } else {
      int val = tab[idx].first;
      c = tab[idx].second;
      if(c == 'L') {
        cout << min(val - 1 + r, l - val) << '\n';
      } else {
        cout << min(val - 1 + l, r - val) << '\n';
      }
    }
  }
  return 0;
}
