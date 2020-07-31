#include <bits/stdc++.h>
using namespace std;

typedef long long Long;

const int N = 1e5 + 5;
const long double OO = 1e20;

int a[N];
int b[N];

int n;
int p;

bool Check(long double t) {
  long double needed = 0;

  for (int i = 0; i < n; ++i) {
    needed += max((long double) 0.0, t * a[i] - b[i]) / p;
  }

  return needed <= t;
}

long double Solve() {
  long double low = 0, high = OO, mid, ans = 0;

  for (int i = 0; i < 2e2; ++i) {
    mid = (low + high) / 2;
    if (Check(mid)) {
      low = mid;
      ans = mid;
    } else {
      high = mid;
    }
  }

  return ans;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#endif

  cin >> n >> p;

  for (int i = 0; i < n; ++i) {
    cin >> a[i] >> b[i];
  }

  auto res = Solve();

  if (res >= 2 * OO / 3) {
    cout << -1;
    return 0;
  }

  cout << fixed << setprecision(6) << res << '\n';

  return 0;
}
