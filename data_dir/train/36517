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

const int N = 1e5 + 5;

vector<int> adj[N];
vector<array<int, 2>> guests;

bool vis_flavor[N];
bool vis_guest[N];

int dfs_guest(int ind);

int dfs_flavor(int flavor) {
  int res = 0;
  for (int v : adj[flavor]) {
    res += dfs_guest(v);
  }
  return res;
}

int dfs_guest(int ind) {
  if (vis_guest[ind]) return 0;

  vis_guest[ind] = true;
  int res = 0;
  bool happy = false;
  vector<int> v;
  for (int flavor : guests[ind]) {
    if (vis_flavor[flavor]) continue;
    happy = true;
    vis_flavor[flavor] = true;
    v.push_back(flavor);
  }

  for (int f : v) {
    res += dfs_flavor(f);
  }

  res += happy;
  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n, k;
  cin >> n >> k;

  for (int i = 0; i < k; ++i) {
    int x, y;
    cin >> x >> y;
    guests.emplace_back(array<int, 2> { x, y });
    adj[x].push_back(i);
    adj[y].push_back(i);
  }

  int res = 0;
  for (int i = 0; i < k; ++i) {
    res += dfs_guest(i);
  }

  cout << k - res << endl;

}
