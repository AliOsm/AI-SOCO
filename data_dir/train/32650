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

const int N = 101;
char res[N][N];
char grid[N][N];

int r, c, k;

string order;

void init() {
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      res[i][j] = '-';
    }
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

  for (char c = 'a'; c <= 'z'; ++c) {
    order += c;
  }
  for (char c = 'A'; c <= 'Z'; ++c) {
    order += c;
  }
  for (char c = '0'; c <= '9'; ++c) {
    order += c;
  }

  while (t--) {
    cin >> r >> c >> k;
    init();
    int cnt_rice = 0;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cin >> grid[i][j];
        cnt_rice += (grid[i][j] == 'R');
      }
    }

    int curr_i = 0, curr_j = 0, dir = 1;
    for (int i = 0; i < k; ++i) {
      int x = cnt_rice / k + bool(i < (cnt_rice % k));
      while (x != 0 || (i == k - 1 && (curr_i < r))) {
        if (grid[curr_i][curr_j] == 'R') {
          --x;
        }
        res[curr_i][curr_j] = order[i];
        if (0 <= curr_j + dir && curr_j + dir < c) {
          curr_j += dir;
        } else {
          ++curr_i;
          dir *= -1;
        }
      }
    }
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cout << res[i][j];
      }
      cout << endl;
    }
  }
}
