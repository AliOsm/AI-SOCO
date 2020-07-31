#include <bits/stdc++.h>

using namespace std;

const int N = 3e5 + 5;

int a[2][N], last[3][N];
map<int, int> dp[2][N];
int ans[N];

int upd(int s, int i, int to, int val) {
  auto it = dp[s][i].find(val);
  if (it == dp[s][i].end()) {
    dp[s][i][val] = to;
  } else {
    dp[s][i][val] = min(dp[s][i][val], to);
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < n; j++) {
      scanf("%d", &a[i][j]);
    }
  }
  map<long long, int> mp[3];
  for (int i = 0; i < 3; i++) {
    mp[i][0] = n;
    last[i][n] = n + 1;
  }
  long long sum[3];
  memset(sum, 0, sizeof(sum));
  for (int i = n - 1; i >= 0; i--) {
    for (int j = 0; j < 3; j++) {
      if (j != 0) sum[j] += a[1][i];
      if (j != 1) sum[j] += a[0][i];
      last[j][i] = last[j][i+1];
      auto it = mp[j].find(sum[j]);
      if (it != mp[j].end()) {
        last[j][i] = min(last[j][i], it->second);
      }
      mp[j][sum[j]] = i;
      //printf("%d %d %d\n", j, i, last[j][i]);
    }
  }
  for (int i = 0; i < n; i++) {
    upd(0, i, last[1][i], ans[i] + 1);
    upd(1, i, last[0][i], ans[i] + 1);
    ans[last[2][i]] = max(ans[last[2][i]], ans[i] + 1);
    ans[i + 1] = max(ans[i + 1], ans[i]);
    for (int j = 0; j < 2; j++) {
      int b = j ^ 1;
      auto it = dp[j][i].find(ans[i] + 1);
      if (it == dp[j][i].end()) continue;
      ans[it->second] = max(ans[it->second], it->first);
      if (last[j][i] < it->second) {
        upd(j, last[j][i], it->second, it->first + 1);
      } else if (last[j][i] > it->second) {
        upd(b, it->second, last[j][i], it->first + 1);
      } else {
        ans[it->second] = max(ans[it->second], it->first + 1);
      }
    }
  }
  cout << ans[n] << endl;
  return 0;
}
