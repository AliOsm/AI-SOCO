#include <bits/stdc++.h>

#include <ext/numeric>

using namespace std;
using namespace __gnu_cxx;
typedef long long Long;

const int MOD = 998244353;

const int N = 3e5 + 5;

vector<int> adj[N];

int memo[N][2][2];

int solve(int root, int parent, bool can_take, bool parent_edge_taken) {
  int& res = memo[root][can_take][parent_edge_taken];
  if (res != -1) return res;
  res = 0;
  array<int, 2> ways;
  ways[0] = 1;  // without taking root.
  ways[1] = 1;  // with taking root.

  for (int v : adj[root]) {
    if (v == parent) continue;
    // Take or leave edge but do not take root.
    ways[0] = (1LL * ways[0] *
               (solve(v, root, true, true) + solve(v, root, true, false))) %
              MOD;

    // Take or leave edge but take root.
    ways[1] = (1LL * ways[1] *
               (solve(v, root, true, false) + solve(v, root, false, true))) %
              MOD;
  }
  if (!parent_edge_taken) {
    int tmp = 1;
    for (int v : adj[root]) {
      if (v == parent) continue;
      tmp = 1LL * tmp * solve(v, root, true, false) % MOD;
    }
    ways[1] = (ways[1] - tmp + MOD) % MOD;
  }
  res = ways[0];
  if (can_take) {
    res = (res + ways[1]) % MOD;
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);
#ifdef Local
  freopen("test.in", "r", stdin);
#endif
  memset(memo, -1, sizeof memo);
  int n;
  cin >> n;
  for (int i = 1; i < n; ++i) {
    int u, v;
    cin >> u >> v;
    adj[u].emplace_back(v);
    adj[v].emplace_back(u);
  }
  cout << (solve(1, -1, true, false) - 1 + MOD) % MOD << endl;
  return 0;
}