#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int x;
  cin >> x;
  for (int a = 1; a <= x; ++a) {
    for (int b = 1; b <= x; ++b) {
      if (a % b != 0) continue;
      if (a * b <= x) continue;
      if (a >= x * b) continue;
      cout << a << " " << b << endl;
      return 0;
    }
  }

  cout << -1;

}
