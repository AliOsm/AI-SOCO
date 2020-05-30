#include <bits/stdc++.h>

using namespace std;

const int N = 1005;

int a[N], n;
int ans0, ans1;


map<string, int> cache;

int ask() {
  string str;
  for (int i = 1; i <= n; i++) str.push_back(a[i] + '0');
  if (cache[str]) return cache[str];

  printf("? ");
  for (int i = 1; i <= n; i++) printf("%d", a[i]);
  printf("\n");
  fflush(stdout);

  int v;
  scanf("%d", &v);
  return cache[str] = v;
}

void dfs(int l, int r, int ask0, int ask1) {
  if (l == r) {
    if (ask0) ans0 = l;
    if (ask1) ans1 = l;
    return;
  }
  if (ask0 == 0 && ask1 == 0) return;
  int mid = (l + r) >> 1;
  int num = r - mid;
  for (int i = mid + 1; i <= r; i++) a[i] = 0;
  int first = ask();
  for (int i = mid + 1; i <= r; i++) a[i] = 1;
  int second = ask();

  if (first + num == second) {
    if (ask0) ans0 = r;
    dfs(l, mid, 0, ask1);
  } else if (first - num == second) {
    if (ask1) ans1 = r;
    dfs(l, mid, ask0, 0);
  } else {
    dfs(mid + 1, r, ask0, ask1);
  }
}

int main() {
  scanf("%d", &n);
  dfs(1, n, 1, 1);
  printf("! %d %d\n", ans0, ans1);
  fflush(stdout);
  return 0;
}
