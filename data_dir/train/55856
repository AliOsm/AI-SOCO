#ifndef Local
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma comment(linker, "/STACK:1024000000,1024000000")
#endif

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

// gp_hash_table<int, int> table;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 1e5 + 5;

struct Point {
  Long x, y;
};

Long dist(const Point& a, const Point& b) {
  Long dx = a.x - b.x;
  Long dy = a.y - b.y;
  return dx * dx + dy * dy;
}

pair<Long, Long> getSlope(const Point& a, const Point& b) {
  pair<Long, Long> res;
  res.first = a.x - b.x;
  res.second = a.y - b.y;
  Long g = __gcd(res.first, res.second);
  res.first /= g, res.second /= g;
  if (res.first < 0) {
    res.first *= -1;
    res.second *= -1;
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n;
  cin >> n;

  if (n & 1) {
    cout << "NO" << endl;
    return 0;
  }

  vector<Point> points(n);
  for (auto& p : points) {
    cin >> p.x >> p.y;
  }

  for (int i = 0; i < n; ++i) {
    int a = i, b = (i + 1) % n;
    int c = (a + n / 2) % n, d = (c + 1) % n;
    Long d1 = dist(points[a], points[b]);
    Long d2 = dist(points[c], points[d]);

    auto slope1 = getSlope(points[a], points[b]);
    auto slope2 = getSlope(points[c], points[d]);

    if (d1 != d2 || slope1 != slope2) {
      cout << "NO" << endl;
      return 0;
    }
  }

  cout << "YES" << endl;

  return 0;
}
