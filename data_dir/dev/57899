#include <bits/stdc++.h>
using namespace std;

const int N = 5003;
const int A = 'z' - 'a' + 1;
const int MOD = round(1e9 + 7);
int memo[N][N];
int d[A];

int Modize(int x) {
  if (x < 0) x += MOD;
  if (x >= MOD) x -= MOD;
  return x;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
//  freopen("out.txt", "w", stdout);
#endif

  int n;
  cin >> n;
  string s;
  cin >> s;

  for (char& c : s) {
    c -= 'a';
  }

  for (int i = 0; i <= n; ++i) {
    memo[n][i] = 1;
  }

  for (int i = n - 1; i >= 0; --i) {
    memset(d, 0, sizeof d);
    int curr = 0;
    for (int j = n - 1; j >= 0; --j) {
      curr = Modize(curr + memo[i + 1][j] - d[s[j]]);
      d[s[j]] = memo[i + 1][j];
      memo[i][j] = curr;
    }
  }

  cout << memo[0][0];
}
