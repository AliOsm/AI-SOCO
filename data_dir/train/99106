#include <bits/stdc++.h>
using namespace std;

typedef long long Long;
typedef long double LDouble;

const int N = 1e5 + 5;

struct Rectangle {
  int x1, x2;
  int y1, y2;
} rect;

struct Mouse {
  int rx, ry;
  LDouble vx, vy;

  LDouble first = -1;
  LDouble last = -1;

  void Calc() {
    LDouble first_x, first_y, last_x, last_y;

    if (rx <= rect.x1) {
      if (round(vx) <= 0) {
        cout << -1;
        exit(0);
      }

      first_x = (rect.x1 - rx) / vx;
      last_x = (rect.x2 - rx) / vx;

    } else if (rx >= rect.x2) {
      if (round(vx) >= 0) {
        cout << -1;
        exit(0);
      }

      first_x = (rect.x2 - rx) / vx;
      last_x = (rect.x1 - rx) / vx;

    } else {
      first_x = 0;
      if (round(vx) == 0) {
        last_x = 1e16;
      } else if (vx > 0) {
        last_x = (rect.x2 - rx) / vx;
      } else {
        last_x = (rect.x1 - rx) / vx;
      }
    }

    // No time for clean code. :(

    if (ry <= rect.y1) {
      if (round(vy) <= 0) {
        cout << -1;
        exit(0);
      }

      first_y = (rect.y1 - ry) / vy;
      last_y = (rect.y2 - ry) / vy;

    } else if (ry >= rect.y2) {
      if (round(vy) >= 0) {
        cout << -1;
        exit(0);
      }

      first_y = (rect.y2 - ry) / vy;
      last_y = (rect.y1 - ry) / vy;

    } else {
      first_y = 0;
      if (round(vy) == 0) {
        last_y = 1e16;
      } else if (vy > 0) {
        last_y = (rect.y2 - ry) / vy;
      } else {
        last_y = (rect.y1 - ry) / vy;
      }
    }

    first = max(first_x, first_y);
    last = min(last_x, last_y);

  }

} mice[N];

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
//  freopen("out.txt", "w", stdout);
#endif

  int n;

  cin >> n;
  cin >> rect.x1 >> rect.y1 >> rect.x2 >> rect.y2;

  if (rect.x1 > rect.x2) {
    swap(rect.x1, rect.x2);
  }
  if (rect.y1 > rect.y2) {
    swap(rect.y1, rect.y2);
  }

  LDouble first = 0, last = 1e16;

  for (int i = 0; i < n; ++i) {
    cin >> mice[i].rx >> mice[i].ry >> mice[i].vx >> mice[i].vy;
    mice[i].Calc();

    first = max(first, mice[i].first);
    last = min(last, mice[i].last);
  }

  if (last < first + 1e-10) {
    cout << -1;
    return 0;
  }

  cout << fixed << setprecision(9) << first;

  return 0;
}
