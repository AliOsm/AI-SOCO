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

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  string s;
  cin >> s;
  int k = count(s.begin(), s.end(), '0') - count(s.begin(), s.end(), '1');
  if (k <= 0) {
    cout << -1 << endl;
    return 0;
  }

  vector<vector<int>> res(k);
  int zereos = 0, ones = 0;

  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == '0') {
      if (!res[zereos].empty() && s[res[zereos].back() - 1] == '0') {
        cout << -1 << endl;
        return 0;
      }
      res[zereos].emplace_back(i + 1);
      zereos = (zereos + 1) % k;
    } else {
      if (!res[ones].empty() && s[res[ones].back() - 1] == '1') {
        cout << -1 << endl;
        return 0;
      }
      res[ones].emplace_back(i + 1);
      ones = (ones + 1) % k;
    }
  }

  cout << k << endl;
  for (auto& x : res) {
    cout << x.size() << " ";
    for (int x : x) {
      cout << x << " ";
    }
    cout << endl;
  }

}
