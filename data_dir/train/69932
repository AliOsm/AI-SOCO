#include <bits/stdc++.h>

using namespace std;

const int N = 3005;

vector<int> edge[N], rev[N];
vector<tuple<int, int, int>> que[N];  // from, k, id
bool can[N], done[N];

int dir[N];
int to_goal[N], ans[N * N];
vector<int> edir[N];
int par[N][15];

void sebar(int now, int source) {
  if (can[now]) return;
  can[now] = 1;
  for (auto it : rev[now]) sebar(it, source);
}

void dfs(int now, int goal) {
  if (done[now]) return;
  done[now] = 1;
  if (now == goal) return;
  for (auto it : edge[now]) if (can[it]) {
    //printf("%d pilih %d\n", now, it);   
    dir[now] = it;
    dfs(it, goal);
    return;
  }
}

void dfs_goal(int now) {
  for (auto it : edir[now]) {
    to_goal[it] = to_goal[now] + 1;
    dfs_goal(it);
  }
}

int main() {
  int n, m, q;
  scanf("%d %d %d", &n, &m, &q);
  for (int i = 0; i < m; i++) {
    int u, v;
    scanf("%d %d", &u, &v);
    edge[u].push_back(v);
    rev[v].push_back(u);
  }
  for (int i = 0; i < q; i++) {
    int from, to, k;
    scanf("%d %d %d", &from, &to, &k);
    que[to].emplace_back(from, k, i);
  }
  for (int i = 1; i <= n; i++) sort(edge[i].begin(), edge[i].end());
    /*
  for (int i = 1; i <= n; i++) {
    for (auto it : edge[i]) {
      printf("%d %d\n", i, it);
    }
  }
  */
  //puts("good one");
  for (int i = 1; i <= n; i++) {
    memset(can, 0, sizeof(can));
    sebar(i, i);
    /*
    for (int j = 1; j <= n; j++) {
      printf("%d %d %d\n", j, i, can[j]);
    }
    */
    //puts("sebar done");
    memset(dir, 0, sizeof(dir));
    memset(done, 0, sizeof(done));
    for (auto it : que[i]) {
      int from;
      tie(from, ignore, ignore) = it;
      dfs(from, i);
    }
    //printf("tema %d\n", i);
    //for (int j = 1; j <= n; j++) printf("dir %d %d\n", j, dir[j]);
    //puts("dfs done");
    memset(to_goal, 0, sizeof(to_goal));
    for (int j = 1; j <= n; j++) {
      edir[j].clear();
    }
    for (int j = 1; j <= n; j++) {
      if (dir[j]) {
        edir[dir[j]].push_back(j);
      }
    }
    to_goal[i] = 1;
    dfs_goal(i);
    for (int j = 1; j <= n; j++) {
      par[j][0] = dir[j];
    }
    for (int k = 1; k < 15; k++) {
      for (int j = 1; j <= n; j++) {
        par[j][k] = par[par[j][k - 1]][k - 1];
      }
    }
    //puts("dfs goal ok");
    for (auto it : que[i]) {
      int from, k, id;
      tie(from, k, id) = it;
      if (to_goal[from] < k) {
        ans[id] = -1;
      } else {
        ans[id] = from;
        k--;
        for (int j = 0; j < 15; j++) {
          if (k & (1 << j)) {
            ans[id] = par[ans[id]][j];
          }
        }
      }
    }
    //puts("done");
  }
  for (int i = 0; i < q; i++) printf("%d\n", ans[i]);
  return 0;
}
