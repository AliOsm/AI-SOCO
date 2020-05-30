#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define all(x) x.begin(), x.end()
#define boost() ios_base :: sync_with_stdio(0); cin.tie(); cout.tie(); cout << fixed; cout << setprecision(15); srand(time(NULL))
#define endl '\n'
#define int long long
const int _N = 1e5 + 11;
const int INF = 1e18 + 11;
const int MOD = 1e9 + 7;
const double EPS = 1e-7;

int n, k, q, x, y, res = 0, d[_N];
vector <int> v[_N], st[_N * 4];

void build (int p, int l, int r) {
  if (l == r) st[p].pb(d[l]);
  else {
    build (2 * p, l, (l + r) / 2);
    build (2 * p + 1, (l + r) / 2 + 1, r);
    int sz_le = st[2 * p].size(), sz_ri = st[2 * p + 1].size();
    int le = 0, ri = 0;
    while (le < sz_le && ri < sz_ri) st[p].pb((st[2 * p][le] < st[2 * p + 1][ri]) ? (st[2 * p][le++]) : (st[2 * p + 1][ri++]));
    while (le < sz_le) st[p].pb(st[2 * p][le++]);
    while (ri < sz_ri) st[p].pb(st[2 * p + 1][ri++]);
  }
}

int query (int p, int l, int r, int L, int R, int x) {
  if (l > r || l > R || r < L) return 0;
  if (l >= L && r <= R) return upper_bound(all(st[p]), x) - st[p].begin();
  return query (2 * p, l, (l + r) / 2, L, R, x) + query(2 * p + 1, (l + r) / 2 + 1, r, L, R, x);
}

signed main () {
  boost();
  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    cin >> x;
    v[x].pb(i);
  }
  for (int i = 1; i <= 100000; i++) {
    if (v[i].empty()) continue;
    for (int j = 0; j < (int)v[i].size(); j++) {
      d[v[i][j]] = ((j + k < (int)v[i].size()) ? (v[i][j + k]) : (n));
    }
  }
  //for (int i = 0; i < n; i++) cout << d[i] << " "; cout << endl;
  build (1, 0, n - 1);
  //for (int i = 0; i < st[1].size(); i++) cout << st[1][i] << " "; cout << endl;
  cin >> q;
  while (q--) {
    cin >> x >> y;
    int l = (res + x) % n;
    int r = (res + y) % n;
    if (l > r) swap(l, r);
    //cout << x << " " << y << " : " << l + 1 << " " << r + 1 << endl;
    res = r - l + 1 - query(1, 0, n - 1, l, r, r);
    cout << res << endl;
  }
  return 0;
}

