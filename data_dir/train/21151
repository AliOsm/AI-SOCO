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

int main() {
  srand(time(0));
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n;
  cin >> n;

  vector<int> arr(n);
  for (int& x : arr) {
    cin >> x;
  }

  int res = 0;
  for (int i = 0; i + 1 < n; ++i) {
    int x = arr[i], y = arr[i + 1];
    if (min(x, y) > 1) {
      cout << "Infinite\n";
      return 0;
    }
    if (i >= 1 && arr[i - 1] == 3 && arr[i + 1] == 2) {
      res += 2;
    } else {
      res += max(x, y) + 1;
    }
  }

  cout << "Finite\n";
  cout << res;

}
