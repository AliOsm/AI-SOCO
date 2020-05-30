#include <bits/stdc++.h>

#include <ext/numeric>

#define all(v) begin(v), end(v)

using namespace std;
using namespace __gnu_cxx;
typedef long long Long;

struct Color {
  int l, p;
};

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n, m;
  cin >> n >> m;
  vector<Color> colors(m);

  for (int i = 0; i < m; ++i) {
    cin >> colors[i].l;
    colors[i].p = -1;
  }

  int used = 0;
  for (int i = m - 1; i >= 0; --i) {
    used = max(used + 1, colors[i].l);
    colors[i].p = n - used + 1;
  }

  if (used > n) {
    cout << -1 << endl;
    return 0;
  }

  int nxt = 1;
  for (int i = 0; i < m; ++i) {
    colors[i].p = min(colors[i].p, nxt);
    nxt = colors[i].p + colors[i].l;
  }

  if (nxt != n + 1) {
    cout << -1 << endl;
    return 0;
  }

  for (auto& color : colors) {
    cout << color.p << " ";
  }
  cout << endl;
  return 0;
}
