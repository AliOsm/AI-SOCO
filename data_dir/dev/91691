#include <bits/stdc++.h>
using namespace std;
#define ll long long
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
const int N = 2e5 + 9, OO = 1e9;

ll arr[N];
vector<ll> vec;

int main() {
  debug();
  int n, m, a, mx = 0, mn = 1e9;
  cin >> n >> m;
  for (int i = 0; i < n; ++i) {
    cin >> a;
    ++arr[a];
    mn = min(mn, a);
    mx = max(mx, a);
  }
  if(mx == mn) {
    cout << 0;
    return 0;
  }
  ll cnt = 0;
  for (int i = mx; i > mn; --i) {
    cnt = arr[i] + cnt;
    vec.push_back(cnt);
  }
  for (int i = 1; i < (int)vec.size(); ++i)
    vec[i] += vec[i - 1];
//  for(auto it: vec)
//    cout << it << endl;
  ll ans = 0, total = 0;
  while(1) {
    int pos = upper_bound(all(vec), total + m) - vec.begin();
    --pos;
    if(pos == (int)vec.size() - 1) {
      ++ans;
      break;
    }
    total = vec[pos];
    ++ans;
  }
  cout << ans;
}
