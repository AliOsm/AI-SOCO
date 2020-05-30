#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#endif

  int a, b, c;
  cin >> a >> b >> c;

  int n;
  cin >> n;

  int res = 0;

  while (n--) {
    int x;
    cin >> x;
    res += (x > b && x < c);
  }

  cout << res;

}
