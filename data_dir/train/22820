#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e3 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;

int main() {
  fastIO;

  int t,
  n;
  cin >> t;
  string str;
  while (t--) {
    cin >> n >> str;
    int arr[10];
    clr(arr, 0);
    for (int i = 0; i < n; ++i)
      ++arr[str[i] - '0'];
    string res(n, '0');
    int mn = 0;
    int i = 0;
    while (i < n) {
      bool en = 0;
      for (int j = mn; j <= 9; ++j) {
        if (arr[j]) {
          mn = j;
          en = 1;
          break;
        }
      }
      if(!en)
        break;
      while (arr[mn] && i < n) {
        if (str[i] - '0' == mn)
          res[i] = '1',--arr[str[i] - '0'];
        ++i;
      }
    }
    i = 0;
    while (i < n) {
      bool en = 0;
      for (int j = mn; j <= 9; ++j) {
        if (arr[j]) {
          en = 1;
          mn = j;
          break;
        }
      }
      if(!en)
        break;
      while (arr[mn] && i < n) {
        if (str[i] - '0' == mn)
          res[i] = '2',--arr[str[i] - '0'];
        ++i;
      }
    }
    bool can = 1;
    for (int j = 0; j < n; ++j)
      can &= (res[j] != '0');
    if (!can)
      cout << '-';
    else {
      for (int j = 0; j < n; ++j) {
        cout << res[j];
      }
    }
    cout << '\n';

  }
  return 0;
}
