#include <bits/stdc++.h>
using namespace std;

map<int, int> fx, fy;
set<int> facs;
vector<int> f;

int power(int a, int b) {
  if (b == 0) return 1;
  int tmp = power(a, b / 2);
  tmp = tmp * tmp;
  if (b & 1) {
    tmp = tmp * a;
  }
  return tmp;
}

map<int, int> factors(int n) {
  map<int, int> mp;
  for (int i = 2; i * i <= n; i++) {
    int cnt = 0;
    while (n % i == 0) {
      cnt++;
      n /= i;
    }
    if (cnt) {
      mp[i] = cnt;
    }
  }
  if (n != 1) {
    mp[n] = 1;
  }
  return mp;
}

int main() {
  int l, r, x, y;
  scanf("%d %d %d %d", &l, &r, &x, &y);
  fx = factors(x);
  fy = factors(y);
  for (auto it : fx) facs.insert(it.first);
  for (auto it : fy) facs.insert(it.first);

  for (auto it : facs) {
    f.push_back(it);
    if (fx[it] > fy[it]) {
      puts("0");
      return 0;
    }
  }
  set<pair<int, int>> ans;
  for (int mask = 0; mask < (1 << facs.size()); mask++) {
    int p = 1, q = 1;
    for (int i = 0; i < facs.size(); i++) {
      if (mask & (1 << i)) {
        p *= power(f[i], fy[f[i]]);
        q *= power(f[i], fx[f[i]]);
      } else {
        q *= power(f[i], fy[f[i]]);
        p *= power(f[i], fx[f[i]]);
      }
    }
    if (l <= p && p <= r && l <= q && q <= r) {
      ans.insert(make_pair(p, q));
      //printf("%d %d\n", p, q);
    }
  }
  cout << ans.size() << endl;

  return 0;
}
