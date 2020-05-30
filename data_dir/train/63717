#include <bits/stdc++.h>

using namespace std;

const int N = 55;
const int BIT = 60;

long long a[N], s[N];
int vis[N][N];

long long find(int l, int r) {
  return s[r] - s[l-1];
}

set<int> edge[N], ori[N];

int dfs(int i, int j) {
  if (i == 0) {
    if (j == 0) return 1;
    return 0;
  }
  if (j <= 0) return 0;
  if (vis[i][j] != -1) return vis[i][j];
  for (auto it : edge[i]) {
    if (dfs(it, j - 1)) {
      return vis[i][j] = 1;
    }
  }
  return vis[i][j] = 0;
}

int main() {
  int n, k;
  scanf("%d %d", &n, &k);
  for (int i = 1; i <= n; i++) scanf("%lld", a + i), s[i] = s[i - 1] + a[i];
  
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < i; j++) {
      edge[i].insert(j);
    }
  }
  
  long long ans = 0;
  for (int bit = BIT - 1; bit >= 0; bit--) {
    for (int i = 1; i <= n; i++) ori[i] = edge[i];
    for (int i = 1; i <= n; i++) {
      for (auto it : ori[i]) {
        if ((find(it + 1, i) & (1LL << bit)) == 0) {
          edge[i].erase(it);
        }
      }
    }
    memset(vis, -1, sizeof(vis));
    bool ret = dfs(n, k);
    if (!ret) {
      for (int i = 1; i <= n; i++) edge[i] = ori[i];
    } else {
      ans += (1LL << bit);
    }
  }
  cout << ans << endl;
  return 0;
}
