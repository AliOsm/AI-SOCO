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
int n;

void moveController(int& pos, bool& to_head) {
  if (to_head) {
    --pos;
  } else {
    ++pos;
  }
  if (pos == 1) {
    to_head = false;
  }
  if (pos == n) {
    to_head = true;
  }
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int stowaway, controller;
  cin >> n >> stowaway >> controller;

  string dir;
  cin >> dir >> dir;

  string train;
  cin >> train;

  bool controller_to_head = (dir == "head");

  for (int i = 0; i + 1 < train.size(); ++i) {
    if (train[i] == '0') {
      bool st_tail = (controller < stowaway);
      stowaway += (st_tail ? 1 : -1);
      stowaway = max(stowaway, 1), stowaway = min(stowaway, n);
    } else {
      stowaway = (controller_to_head ? n : 1);
    }
    moveController(controller, controller_to_head);
    if (stowaway == controller) {
      cout << "Controller " << i + 1 << endl;
      return 0;
    }
  }

  cout << "Stowaway" << endl;
  return 0;
}
