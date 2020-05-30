#include <bits/stdc++.h>
using namespace std;

const int N = 1e4;
pair<int, int> ver[N];

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
  cout << fixed << setprecision(7);
  int n, w;
  double v, u, mx;
  cin >> n >> w >> v >> u;
  bool before = 1;
  mx = w / u;
  for (int i = 0; i < n; ++i) {
    cin >> ver[i].first >> ver[i].second;
    double t = ver[i].first / v;
    before &= (t >= ver[i].second / u);
    mx = max(mx, (w - ver[i].second) / u + t);
  }
  if (before)
    cout << w / u;
  else
    cout << mx;
}
