#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e2 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;

vector<int> vec[N];
int vis[N], cnt = 0;

bool DFS(int u, int par){
  if(vis[u])
    return 1;
  vis[u] = 1;
  ++cnt;
  int can = 0;
  for(int it: vec[u]) {
    if(it == par)
      continue;
    can |= DFS(it, u);
  }
  return can;
}

int main() {
  fastIO;
  int n, m, u, v;
  cin >> n >> m;
  for (int i = 0; i < m; ++i) {
    cin >> u >>v;
    vec[u].push_back(v);
    vec[v].push_back(u);
  }
  int ans = 0;
  for (int i = 1; i <= n; ++i) {
    cnt = 0;
    if(DFS(i, 0))
      if(cnt & 1)
        ++ans;
  }
  if((n - ans) & 1)
    ++ans;
  cout << ans;
  return 0;
}
