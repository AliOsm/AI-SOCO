#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;
const int inf = 1e9;

void upd(int& at, int val) {
  at = max(at, val);
}

int dp[N][2];
vector<int> edge[N];
int tmp[2];

void dfs(int now, int bef) {
  dp[now][1] = 0;
  for (auto it : edge[now]) {
    if (it == bef) continue;
    dfs(it, now);
    tmp[0] = tmp[1] = -inf;
    for (int i = 0; i < 2; i++) {
      for (int j = 0; j < 2; j++) {
        for (int k = 0; k < 2; k++) {
          if (k == 1 && j == 1) continue;
          if (k == 0) {
            upd(tmp[i ^ j], dp[now][i] + dp[it][j]);
          } else {
            upd(tmp[i], dp[now][i] + dp[it][j] + 1);
          }
        }
      }
    }
    dp[now][0] = tmp[0];
    dp[now][1] = tmp[1];
  }
}

int main() {
  for (int i = 0; i < N; i++) {
    dp[i][0] = dp[i][1] = -inf;
  }
  int n;
  scanf("%d", &n);
  for (int i = 1; i < n; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    edge[u].push_back(v);
    edge[v].push_back(u);
  }
  dfs(1, 0);
  if (dp[1][0] < 0) dp[1][0] = -1;
  cout << dp[1][0] << endl;
  // for (int i = 1; i <= n; i++) {
  //   printf("%d: %d %d\n", i, dp[i][0], dp[i][1]);
  // }
  return 0;
}
