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

const int N = 61;

char grid[N][N];
int r, c;

bool case1() {
  bool north_border = true;
  bool south_border = true;
  for (int j = 0; j < c; ++j) {
    north_border &= (grid[0][j] == 'A');
    south_border &= (grid[r - 1][j] == 'A');
  }

  bool left_border = true;
  bool right_border = true;
  for (int i = 0; i < r; ++i) {
    left_border &= (grid[i][0] == 'A');
    right_border &= (grid[i][c - 1] == 'A');
  }

  return north_border || south_border || left_border || right_border;
}

bool case2() {
  if (grid[0][0] == 'A' || grid[0][c - 1] == 'A' || grid[r - 1][0] == 'A'
    || grid[r - 1][c - 1] == 'A') return true;
  for (int i = 0; i < r; ++i) {
    bool all_a = true;
    for (int j = 0; j < c; ++j) {
      all_a &= (grid[i][j] == 'A');
    }
    if (all_a) return true;
  }
  for (int j = 0; j < c; ++j) {
    bool all_a = true;
    for (int i = 0; i < r; ++i) {
      all_a &= (grid[i][j] == 'A');
    }
    if (all_a) return true;
  }
  return false;
}

bool case3() {
  for (int i = 0; i < r; ++i) {
    if (grid[i][0] == 'A' || grid[i][c - 1] == 'A') return true;
  }
  for (int j = 0; j < c; ++j) {
    if (grid[0][j] == 'A' || grid[r - 1][j] == 'A') return true;
  }
  return false;
}

int solve() {
  if (case1()) return 1;
  if (case2()) return 2;
  if (case3()) return 3;
  return 4;
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
    cin >> r >> c;
    bool a_appeared = false;
    bool b_appeared = false;
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cin >> grid[i][j];
        a_appeared |= (grid[i][j] == 'A');
        b_appeared |= (grid[i][j] == 'P');
      }
    }
    if (!a_appeared) {
      cout << "MORTAL" << endl;
    } else if (!b_appeared) {
      cout << 0 << endl;
    } else {
      cout << solve() << endl;
    }
  }
}