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

// gp_hash_table<int, int> table;

const int N = 2003;

Long cost[N][N];
Long dist[N];
int parent[N];
int vis[N];
int vis_id;
const Long OO = (Long) 1e17;
int n;

Long prim(int src, vector<pair<int, int>>& edges) {
  edges.clear();
  ++vis_id;
  fill(dist, dist + n, OO);
  dist[src] = 0;
  Long res = 0;
  while (src != -1) {
    vis[src] = vis_id;
    int nxt = -1;
    Long mn = OO;
    for (int i = 0; i < n; i++) {
      if (cost[src][i] < dist[i]) {
        dist[i] = cost[src][i];
        parent[i] = src;
      }
      if (vis[i] != vis_id && dist[i] < mn) {
        mn = dist[i];
        nxt = i;
      }
    }
    if (nxt != -1) {
      edges.emplace_back(nxt, parent[nxt]);
      res += mn;
    }
    src = nxt;
  }
  return res;
}

Long x[N], y[N], c[N], k[N];
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  cin >> n;

  for (int i = 0; i < n; ++i) {
    cin >> x[i] >> y[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> c[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> k[i];
  }
  for (int i = 0; i < n; ++i) {
    cost[i][n] = cost[n][i] = c[i];
    for (int j = 0; j < n; ++j) {
      cost[i][j] = (abs(x[i] - x[j]) + abs(y[i] - y[j])) * (k[i] + k[j]);
    }
  }
  ++n;

  vector<pair<int, int>> edges;
  cout << prim(0, edges) << endl;

  vector <int> elec;
  for (auto& edge : edges) {
    if (edge.first == n - 1) {
      elec.push_back(edge.second);
    }
    if (edge.second == n - 1) {
      elec.push_back(edge.first);
    }
  }
  cout << elec.size() << endl;
  for (int x : elec) {
    cout << x + 1  << " ";
  }
  cout << endl;
  cout << edges.size() - elec.size() << endl;
  for (auto& edge : edges) {
    if (edge.first != n - 1 && edge.second != n - 1) {
      cout << edge.first + 1 << " " << edge.second + 1 << endl;
    }
  }

}
