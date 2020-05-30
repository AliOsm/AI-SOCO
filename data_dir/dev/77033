#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;

long long a[N], lef[N], rig[N];

int main() {
  int n;
  long long p, q, r;
  scanf("%d %lld %lld %lld", &n, &p, &q, &r);
  for (int i = 0; i < n; i++) {
    scanf("%lld", a + i);
  }
  for (int i = 0; i < N; i++) lef[i] = rig[i] = -4e18;
  for (int i = 0; i < n; i++) {
    if (i) lef[i] = lef[i - 1];
    lef[i] = max(lef[i], p * a[i]);
  }
  for (int i = n - 1; i >= 0; i--) {
    if (i + 1 < n) rig[i] = rig[i + 1];
    rig[i] = max(rig[i], r * a[i]);
  }
  long long ans = -4e18;
  for (int i = 0; i < n; i++) {
    //cout << lef[i] + rig[i] + q * a[i] << endl;
    ans = max(ans, lef[i] + rig[i] + q * a[i]);
  }
  cout << ans << endl;
  return 0;
}
