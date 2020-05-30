#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e5 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;

int par[N], sz[N];

int find(int x) {
  if(x == par[x]) return x;
  return par[x] = find(par[x]);
}

void join(int x, int y) {
  x = find(x), y = find(y);
  if(x == y)
    return ;
  if(sz[x] < sz[y])
    swap(x, y);
  par[y] = x;
  sz[x] += sz[y];
  return;
}

int main() {
  fastIO;

  int n,
  k;
  cin >> n >> k;
  for (int i = 1; i <= n; ++i)
    par[i] = i, sz[i] = 1;
  int u, v;
  int total = 0;
  for (int i = 0; i < k; ++i) {
    cin >> u >> v;
    join(u, v);
  }
  for (int i = 1; i <= n; ++i) {
    if(find(i) == i)
      total += sz[i] - 1;
  }
  cout << (k - total);
  return 0;
}
