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
const int N = 5e5 + 9, OO = 1e9;

ll par[N], sz[N];

ll find(ll x) {
  if(x == par[x]) return x;
  return par[x] = find(par[x]);
}

void join(ll x, ll y) {
  x = find(x), y = find(y);
  if(x != y) {
    if(sz[x] < sz[y]) swap(x, y);
    par[y] = x;
    sz[x] += sz[y];
  }
}

int main() {
  debug();
  ll n, m, k, a, prv;
  cin >> n >> m;
  for (int i = 1; i <= n; ++i) {
    sz[i] = 1;
    par[i] = i;
  }
  for (int i = 0; i < m; ++i) {
    cin >> k;
    prv = -1;
    for (int j = 0; j < k; ++j) {
      cin >> a;
      if(prv != -1) {
        join(prv, a);
      }
      prv = a;
    }
  }
  int v;
  for (int i = 1; i <= n; ++i) {
    v = find(i);
    cout << sz[v] << " ";
  }
  return 0;
}
