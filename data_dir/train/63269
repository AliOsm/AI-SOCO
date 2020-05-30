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

string solve(vector<pair<char, int>> vec) {
  int iter = 5000;
  while (iter--) {
    random_shuffle(vec.begin(), vec.end());
    bool valid = true;
    for (int i = 0; i + 1 < vec.size(); ++i) {
      valid &= (abs(vec[i].first - vec[i + 1].first) != 1);
    }
    if (valid) {
      string res;
      for (auto& p : vec) {
        res += string(p.second, p.first);
      }
      return res;
    }
  }
  return "No answer";
}

int main() {
  srand(time(0));
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int t;
  cin >> t;

  while (t--) {
    string s;
    cin >> s;
    map<int, int> mp;
    for (char c : s) {
      ++mp[c];
    }
    vector<pair<char, int>> vec(mp.begin(), mp.end());

    cout << solve(vec) << endl;

  }

}
