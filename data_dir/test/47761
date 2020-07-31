#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, M = 1e6 + 9, OO = 1e9 + 9, MOD = 1e9 + 7;

int nxt[N];

int main() {
  fastIO
  int t;
  cin >> t;
  string str;
  while(t--) {
    cin >> str;
    clr(nxt, 0);
    nxt[0] = -1;
    for (int i = 0; i < str.size(); ++i) {
      if(str[i] == '1')
        nxt[i + 1] = i;
      else
        nxt[i + 1] = nxt[i];
    }
    int ans = 0;
    for (int i = 0; i < str.size(); ++i) {
      int n = max(0, i - 20), cur = 0;
      for (int j = i; j >= n; --j) {
        if(str[j] == '0') {
          continue;
        }
        cur += (1 << (i - j));
        if(cur <= i - nxt[j])
          ++ans;
      }
    }
    cout << ans << '\n';
  }
  return 0;
}
