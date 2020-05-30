#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 5;

vector<int> l, e;

int main() {
  int n, m, cl, ce, v;
  scanf("%d %d %d %d %d", &n, &m, &cl, &ce, &v);
  for (int i = 0; i < cl; i++) {
    int num;
    scanf("%d", &num);
    l.push_back(num);
  }
  for (int i = 0; i < ce; i++) {
    int num;
    scanf("%d", &num);
    e.push_back(num);
  }
  sort(l.begin(), l.end());
  sort(e.begin(), e.end());
  int q;
  scanf("%d", &q);
  while (q--) {
    int x1, y1, x2, y2;
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    if (y1 > y2) swap(y1, y2);
    if (x1 == x2) {
      printf("%d\n", y2 - y1);
      continue;
    }
    int best = 1e9;
    int low_e = lower_bound(e.begin(), e.end(), y2) - e.begin() - 1;
    int upp_e = lower_bound(e.begin(), e.end(), y1) - e.begin();
    int low_l = lower_bound(l.begin(), l.end(), y2) - l.begin() - 1;
    int upp_l = lower_bound(l.begin(), l.end(), y1) - l.begin();
    if (0 <= low_e && low_e < e.size()) {
      int d = abs(x1 - x2);
      int add = (d / v + (d % v? 1 : 0));
      best = min(best, abs(y1 - e[low_e]) + abs(y2 - e[low_e]) + add);
    }
    if (0 <= upp_e && upp_e < e.size()) {
      int d = abs(x1 - x2);
      int add = (d / v + (d % v? 1 : 0));
      best = min(best, abs(y1 - e[upp_e]) + abs(y2 - e[upp_e]) + add);
    }
    if (0 <= low_l && low_l < l.size()) {
      best = min(best, abs(y1 - l[low_l]) + abs(y2 - l[low_l]) + abs(x1 - x2));
    }
    if (0 <= upp_l && upp_l < l.size()) {
      best = min(best, abs(y1 - l[upp_l]) + abs(y2 - l[upp_l]) + abs(x1 - x2));
    }
    printf("%d\n", best);
  }

  return 0;
}
