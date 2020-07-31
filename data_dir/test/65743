#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int dx[] = { 1, 1, 1, 0, 0, -1, -1, -1 };
int dy[] = { -1, 0, 1, -1, 1, -1, 0, 1 };

const int N = 4;
char grid[N][N];

char Get(int x, int y) {
  if (min(x, y) >= 0 && max(x, y) < N) {
    return grid[x][y];
  }
  return 'o';
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
//  freopen("wa.txt", "w", stdout);
#endif

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> grid[i][j];
    }
  }

  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      for (int d = 0; d < 8; ++d) {
        int dot = 0, xs = 0;
        for (int k = 0; k < 3; ++k) {
          int x = i + k * dx[d];
          int y = j + k * dy[d];
          dot += (Get(x, y) == '.');
          xs += (Get(x, y) == 'x');
        }
        if (xs == 3 || (xs == 2 && dot == 1)) {
          cout << "YES";
          return 0;
        }
      }
    }
  }

  cout << "NO";

}
