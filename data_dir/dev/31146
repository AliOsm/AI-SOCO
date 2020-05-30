#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef unsigned long long ULong;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n;
  cin >> n;
  int res = INT_MAX;
  for (int h = 1; h * h <= n; ++h) {
    int v = (n + h - 1) / h;
    res = min(res, h + v);
  }
  cout << res;
}
