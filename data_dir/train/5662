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
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
 
const int N = 1e5 + 5;
int arr[N];
bool vis[N];
int n;
 
int ask(int i) {
  if (i > n) i -= n;
  if (vis[i]) return arr[i];
  vis[i] = true;
  assert(count(vis, vis + N, true) <= 60);
  cout << "? " << i << endl;
  cin >> arr[i];
  return arr[i];
}
 
int g(int i) {
    return ask(i) - ask(i + n / 2);
}

int solve(int l, int r) {
    int mid = (l + r) / 2;
    int gl = g(l) , gm = g(mid) , gr = g(r);
    if (gl == 0) return l;
    if (gr == 0) return r;
    if (gm == 0) return mid;
    if ((gl > 0) ^ (gm > 0)) return solve(l , mid);
    return solve(mid , r);
}
 
int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
//  freopen("test.in", "r", stdin);
#else
//#define endl '\n'
#endif
 
  cin >> n;
  if (n % 4 != 0) {
    cout << "! -1" << endl;
    return 0;
  }
  int res = solve(1, 1 + n / 2);
  cout << "! " << res << endl;
 
}