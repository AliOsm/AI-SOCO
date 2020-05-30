#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define all(v)    ((v).begin()),((v).end())
#define clr(a,b)  memset(a,b,sizeof(a))
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
// freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}

int const N = 2e5 + 9, OO = 1e9;
bool found[N];
int idx[N], arr[N],teams[N], goot[N];

int main() {
  debug();
  int n, k;
  cin >> n >> k;
  clr(idx, -1);
  clr(goot, -1);
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
    idx[arr[i]] = i, found[i] = 1;
  }
  int cnt = 0, cur = 2, m;
  for (int i = n; i > 0; --i) {
    m = idx[i]; // idx
    if( (m == -1) || (!found[m]))
      continue;
    if(cur == 2)
      cur = 1;
    else
      cur = 2;
    found[m] = 0, cnt = 0, teams[m] = cur;
    int j = m + 1;
    for (j = m + 1; j < n; ++j) {
      if(!found[j]) {
        if(goot[j] != -1)
          j = goot[j];
        continue;
      }
      ++cnt, found[j] = 0, teams[j] = cur;
      if(cnt == k)
        break;
    }
    cnt = 0;
    int jj;
    for (jj = m - 1; jj >= 0; --jj) {
      if(!found[jj]) {
        if(goot[jj] != -1)
          jj = goot[jj];
        continue;
      }
      ++cnt, found[jj] = 0, teams[jj] = cur;
      if(cnt == k)
        break;
    }
    if(jj >= 0 && jj < n)
        goot[jj] = j;
    if(j >= 0 && j < n)
        goot[j] = jj;
  }
  for (int i = 0; i < n; ++i) {
    cout << teams[i];
  }
  return 0;
}