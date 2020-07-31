#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e6 + 9, OO = 1e9 + 9;

vector<ll> vec;
ll arr[N];
map<ll, int> mp;

int main() {
  fastIO;
  int n, k;
  cin >> n >> k;
  ll cur = 1, mx = 1e15;
  for (int i = 0; i < 50; ++i) {
    if(abs(cur) >= mx)
      break;
    vec.push_back(cur);
    cur *= k;
  }
  int m = vec.size();
  if(k == 1)
    m = 1;
  else if(k == -1)
    m = 2;
  for (int i = 1; i <= n; ++i) {
    cin >> arr[i];
    arr[i] += arr[i-1];
  }
  mp[0] = 1;
  ll ans = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j < m; ++j) {
      if(mp.find(arr[i] - vec[j]) != mp.end())
        ans += mp[arr[i] - vec[j]];
    }
    ++mp[arr[i]];
  }
  cout << ans;
  return 0;
}
