#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(9), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, OO = 1e9;


typedef complex<double> point;


#define X real()
#define Y imag()
#define vec(a,b)                ((b)-(a))
#define cp(a,b)                 ( (conj(a)*(b)).imag() )  // a*b sin(T), if zero -> parllel

// Where is P2 relative to segment p0-p1?
// ccw = +1 => angle > 0 or collinear after p1
// cw = -1 => angle < 0 or collinear after p0
// Undefined = 0 => Collinar in range [a, b]. Be careful here
int ccw(point a, point b, point c) {
  point v1(b - a), v2(c - a);
  double t = cp(v1, v2);

  if (t > +EPS)
    return +1;
  if (t < -EPS)
    return -1;
  if (v1.X * v2.X < -EPS || v1.Y * v2.Y < -EPS)
    return -1;
  if (norm(v1) < norm(v2) - EPS)
    return +1;
  return 0;
}

double triangleArea3points(const point &a, const point &b, const point &c) {
  return fabs(cp(a,b) + cp(b, c) + cp(c, a)) / 2;
}

vector<point> pts;
int main() {
//  fastIO;
  int n, a, b;
//  cin >> n;
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) {
//    cin >> a >> b;
    scanf("%d%d", &a, &b);
    pts.push_back(point(a, b));
  }
  double ans = 0, cur;
  for (int i = 0; i < n; ++i) {
    for (int j = i+1; j < n; ++j) {
      double L = EPS, R = EPS;
      for (int k = 0; k < n; ++k) {
        if(k == j || k == i)
          continue;
        cur = (cp(pts[i],pts[j]) + cp(pts[j], pts[k]) + cp(pts[k], pts[i])) / 2;
        if(cur < 0) {
          cur *= -1;
          if(cur - L > EPS)
            L = cur;
        } else {
          if(cur - R > EPS)
            R = cur;
        }
      }
      if(L <= EPS || R <= EPS)
        continue;
      if(L + R - ans > EPS)
        ans = (L + R);
    }
  }
//  cout << ans;
  printf("%lf", ans);
  return 0;
}
