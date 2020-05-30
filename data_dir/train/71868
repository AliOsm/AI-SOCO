#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 5e4 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;

int n, k;
vector<int> vec[N];
ll cnt[N][509], cur;

void DFS(int x, int par) {
  for(int it: vec[x]) {
    if(it == par)
      continue;
    DFS(it, x);
    for (int i = 0; i < k; ++i) {
      int rem = k - i - 1;
      cur += (ll)cnt[x][i] * cnt[it][rem];
    }
    for (int i = 1; i <= k; ++i)
      cnt[x][i] += cnt[it][i-1];
  }
}

int main() {
  fastIO;
  cin >> n >> k;
  int u, v;
  for (int i = 1; i < n; ++i) {
    cin >> u >> v;
    vec[u].push_back(v);
    vec[v].push_back(u);
  }
  ++n;
  for (int i = 1; i <= n; ++i)
    cnt[i][0] = 1;
  DFS(1, 0);
  cout << (cur);
  return 0;
}
