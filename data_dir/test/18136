#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
double const EPS = 1e-15, PI = acos(-1);
const int N = 2e5 + 9, OO = 1e9;

int arr[26];
vector<int> vec;

int main() {
  fastIO;
  int n, m;
  string str;
  cin >> n >> m >> str;
  for (int i = 0; i < n; ++i)
    ++arr[str[i] -'A'];
  for (int i = 0; i < 26; ++i) {
    if(arr[i])
      vec.push_back(arr[i]);
  }
  sort(all(vec), greater<int>());
  ll ans = 0, cnt = 0;
  for (int i = 0; i < (int)vec.size(); ++i) {
    cnt = min(vec[i], m);
    ans += cnt * cnt;
    m -= cnt;
    if(m == 0)
      break;
  }
  cout << ans;
  return 0;
}
