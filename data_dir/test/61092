#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#endif

  int n, k;
  cin >> n >> k;

  double sum = 0;

  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;

    sum += 1LL * x * (min(k, i + 1) - max(1, k - (n - 1 - i)) + 1);
  }

  cout << fixed << setprecision(10) << sum / (n - k + 1);

}
