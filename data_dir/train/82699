#include <bits/stdc++.h>
using namespace std;

const int N = 20004;
int users[N];

int main() {
//  ios::sync_with_stdio(0), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
//  freopen("o.txt", "wt", stdout);
#endif

  deque<int> curr;

  int n, m, t;
  cin >> n >> m >> t;
  --t;
  bool reached = false;
  int cnt_users = 0;
  for (int i = 0; i < n; ++i) {
    int a, b, c;
    char tmp;
    cin >> a >> tmp >> b >> tmp >> c;
    c += 60 * (b + 60 * a);
    while (!curr.empty() && curr.back() < c) {
      curr.pop_back();
    }
    if (curr.size() == m) {
      curr.pop_front();
    } else {
      ++cnt_users;
    }
    users[i] = cnt_users;
    curr.push_front(c + t);
    reached |= curr.size() == m;
  }

  if (!reached) {
    cout << "No solution\n";
  } else {
    cout << cnt_users << '\n';
    for (int i = 0; i < n; ++i) {
      cout << users[i] << '\n';
    }
  }

  return 0;
}
