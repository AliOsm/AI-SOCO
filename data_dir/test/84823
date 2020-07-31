#ifndef Local
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma comment(linker, "/STACK:1024000000,1024000000")
#endif

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 2e5 + 5;
vector<int> adj[N];

int comp[N][2];
int n, m, a, b;

void dfs(int node, int c_id, bool prohibit_a) {
  if (prohibit_a && node == a) return;
  if (!prohibit_a && node == b) return;
  if (comp[node][prohibit_a] == c_id) return;
  comp[node][prohibit_a] = c_id;
  for (int x : adj[node]) {
    dfs(x, c_id, prohibit_a);
  }
}

gp_hash_table<int, int> mp[N];
int cnt_all_a[N];
int cnt_all_b[N];

void clear() {
  for (int i = 1; i <= n; ++i) {
    comp[i][0] = comp[i][1] = 0;
    adj[i].clear();
    mp[i].clear();
    cnt_all_a[i] = cnt_all_b[i] = 0;
  }
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int t;
  cin >> t;

  while (t--) {
    cin >> n >> m >> a >> b;
    while (m--) {
      int u, v;
      cin >> u >> v;
      adj[u].push_back(v);
      adj[v].push_back(u);
    }

    for (int i = 1; i <= n; ++i) {
      if (i == a || i == b) continue;
      if (comp[i][0] == 0) {
        dfs(i, i, false);
      }
      if (comp[i][1] == 0) {
        dfs(i, i, true);
      }
    }

    for (int i = 1; i <= n; ++i) {
      if (i == a || i == b) continue;
      ++mp[comp[i][0]][comp[i][1]];
      ++cnt_all_a[comp[i][0]];
      ++cnt_all_b[comp[i][1]];
    }

    Long res = 0;
    for (int i = 1; i <= n; ++i) {
      if (i == a || i == b) continue;
      res += n - 2 - cnt_all_b[comp[i][1]]
        - (cnt_all_a[comp[i][0]] - mp[comp[i][0]][comp[i][1]]);
    }

    cout << res / 2 << endl;

    clear();
  }
}
