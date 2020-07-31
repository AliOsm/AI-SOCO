#include <bits/stdc++.h>

using namespace std;

const int N = 1e5 + 5;
const int inf = 2e9;

// cost - beauty
vector<pair<int, int>> c, d;

// take c and take d
// beauty, cost, and id
vector<tuple<int, int, int>> tc[N], td[N];

int main() {
  int n, C, D;
  scanf("%d %d %d", &n, &C, &D);
  for (int i = 0; i < n; i++) {
    int b, cost;
    char f;
    scanf("%d %d %c", &b, &cost, &f);
    if (f == 'C') {
      c.emplace_back(cost, b);
    } else {
      d.emplace_back(cost, b);
    }
  }
  sort(c.begin(), c.end());
  sort(d.begin(), d.end());
  for (int i = 0; i < c.size(); i++) {
    if (i) tc[i] = tc[i - 1];
    tc[i].emplace_back(c[i].second, c[i].first, i);
    sort(tc[i].begin(), tc[i].end());
    reverse(tc[i].begin(), tc[i].end());
    vector<tuple<int, int, int>> tmp;
    for (int j = 0; j < min(2, (int) tc[i].size()); j++) {
      tmp.push_back(tc[i][j]);
    }
    tc[i] = tmp;
    //for (auto it : tc[i]) printf("%d: %d %d %d\n", i, get<0>(it), get<1>(it), get<2>(it));
  }
  //cout << d.size() << endl;
  for (int i = 0; i < d.size(); i++) {
    if (i) td[i] = td[i - 1];
    td[i].emplace_back(d[i].second, d[i].first, i);
    sort(td[i].begin(), td[i].end());
    reverse(td[i].begin(), td[i].end());
    vector<tuple<int, int, int>> tmp;
    for (int j = 0; j < min(2, (int) td[i].size()); j++) {
      tmp.push_back(td[i][j]);
    }
    td[i] = tmp;
    //for (auto it : td[i]) printf("%d: %d %d %d\n", i, get<0>(it), get<1>(it), get<2>(it));
  }
  int ans = 0;
  if (c.size() >= 2) {
    for (int i = 0; i < c.size(); i++) {
      // beauty, id
      int cost = c[i].first;
      int beauty = c[i].second;
      if (cost > C) continue;
      int p = lower_bound(c.begin(), c.end(), make_pair(C - cost, inf)) - c.begin() - 1;
      if (p >= 0) {
        for (int j = 0; j < tc[i].size(); j++) {
          for (int k = 0; k < tc[p].size(); k++) {
            if (get<2>(tc[i][j]) == get<2>(tc[p][k])) continue;
            ans = max(ans, get<0>(tc[i][j]) + get<0>(tc[p][k]));
          }
        }
      }
    }
  }
  if (d.size() >= 2) {
    for (int i = 0; i < d.size(); i++) {
      // beauty, id
      set<pair<int, int>> s;
      int cost = d[i].first;
      int beauty = d[i].second;
      if (cost > D) continue;
      int p = lower_bound(d.begin(), d.end(), make_pair(D - cost, inf)) - d.begin() - 1;
      //printf("id %d %d\n", i, p);
      if (p >= 0) {
        for (int j = 0; j < td[i].size(); j++) {
          for (int k = 0; k < td[p].size(); k++) {
            if (get<2>(td[i][j]) == get<2>(td[p][k])) continue;
            ans = max(ans, get<0>(td[i][j]) + get<0>(td[p][k]));
          }
        }
      }
    }
  }
  if (c.size() >= 1 && d.size() >= 1) {
    int p = lower_bound(c.begin(), c.end(), make_pair(C, inf)) - c.begin() - 1;
    int q = lower_bound(d.begin(), d.end(), make_pair(D, inf)) - d.begin() - 1;
    if (p >= 0 && q >= 0) {
      ans = max(ans, get<0>(tc[p][0]) + get<0>(td[q][0]));
    }
  }
  cout << ans << endl;
  return 0;
}
