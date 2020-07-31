#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#pragma GCC target( \
    "sse,sse2,sse3,ssse3,sse4,sse4.2,popcnt,abm,mmx,avx,tune=native")
#pragma comment(linker, "/STACK:1024000000,1024000000")

#include <bits/stdc++.h>

#include <ext/numeric>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
using namespace std;

#define popCnt(x) (__builtin_popcountll(x))
#define all(v) begin(v), end(v)

typedef long long Long;
typedef vector<int> vi;

const int N = 2e5 + 5;

Long calc(Long x, Long y, Long z) {
  return (x - y) * (x - y) + (y - z) * (y - z) + (x - z) * (x - z);
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
    vector<int> sz(3);
    for (int& x : sz) {
      cin >> x;
    }
    vector<vector<int>> w(3);
    for (int i = 0; i < 3; ++i) {
      w[i].resize(sz[i]);
      for (int& x : w[i]) {
        cin >> x;
      }
      sort(w[i].begin(), w[i].end());
      w[i].erase(unique(all(w[i])), end(w[i]));
      sz[i] = w[i].size();
    }
    Long res = LLONG_MAX;
    vector<int> order = {0, 1, 2};

    do {
      int x_ind = 0, y_ind = 0, z_ind = 0;
      int y_mid_ind = 0;
      while (x_ind != sz[order[0]]) {
        while (y_ind != sz[order[1]] &&
               w[order[1]][y_ind] < w[order[0]][x_ind]) {
          ++y_ind;
        }
        if (y_ind == sz[order[1]]) break;
        while (z_ind != sz[order[2]] &&
               w[order[2]][z_ind] < w[order[1]][y_ind]) {
          ++z_ind;
        }
        if (z_ind == sz[order[2]]) break;
        y_mid_ind = max(y_mid_ind, y_ind);

        while (y_mid_ind + 1 != sz[order[1]] &&
               w[order[1]][y_mid_ind + 1] <= w[order[2]][z_ind] &&
               calc(w[order[0]][x_ind], w[order[1]][y_mid_ind + 1],
                    w[order[2]][z_ind]) <= calc(w[order[0]][x_ind],
                                                w[order[1]][y_mid_ind],
                                                w[order[2]][z_ind])) {
          ++y_mid_ind;
        }
        res = min(res, calc(w[order[0]][x_ind], w[order[1]][y_mid_ind],
                            w[order[2]][z_ind]));
        ++x_ind;
      }
    } while (next_permutation(order.begin(), order.end()));
    cout << res << endl;
  }
  return 0;
}
