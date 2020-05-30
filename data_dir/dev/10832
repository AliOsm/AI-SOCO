#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 1000006;
const int A = 10000007;
int dp[A];
int sizes[N];
int n, k;

int Build(int x) {
  memset(dp, 0, sizeof dp);
  for (int i = 0; i < A; ++i) {
    if (i >= x) dp[i] = 1;
    dp[i] = max(dp[i], dp[i / 2] + dp[(i + 1) / 2]);
  }
}

bool Can(int x) {
  Build(x);
  ll res = 0;
  for (int i = 0; i < n; ++i) {
    res += dp[sizes[i]];
  }
  return res >= k;
}

int Bs() {
  int low = 0, high = A, mid, ans;
  while (low <= high) {
    mid = (low + high) / 2;
    if (Can(mid)) {
      ans = mid;
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return ans;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
#endif

  cin >> n >> k;
  for (int i = 0; i < n; ++i) {
    cin >> sizes[i];
  }

  int res = Bs();
  if (res == 0) --res;
  cout << res;

}
