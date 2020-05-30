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

const int N = 1e5 + 5;

int a[N];

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n, m;
  cin >> n >> m;

  vector<string> ans(n);

  for (auto& s : ans) {
    cin >> s;
  }

  for (int i =0 ; i < m ; ++i) {
    cin >> a[i];
  }

  int res = 0;

  for (int i = 0; i < m; ++i) {
    map<char, int> mp;
    int tmp = 0;
    for (int j = 0; j < n; ++j) {
      tmp = max(tmp, ++mp[ans[j][i]]);
    }
    res += tmp * a[i];
  }

  cout << res << endl;

}
