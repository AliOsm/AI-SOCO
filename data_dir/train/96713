#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
//  freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, OO = 1e9;

vector<int> vec[109];

int main() {
  debug();
  int mx = 1e9;
  int n, m;
  cin >> n >> m;
  int cur = 1;
  for (int i = 0; i < m; ++i) {
    int u, v;
    cin >> u >> v;
    vec[u].push_back(cur);
    vec[v].push_back(cur);
    ++cur;
  }
  for (int i = 1; i <= n; ++i) {
    if ((int) vec[i].size() == 0) {
      vec[i].push_back(mx);
      --mx;
    }
    cout << vec[i].size() << '\n';
    for (int it : vec[i]) {
      cout << it << ' ' << i << '\n';
    }
  }
}
