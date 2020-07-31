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
const int N = 1e5 + 9, OO = 1e9;

int main() {
  debug();
  string str;
  cin >> str;
  ll reqa = count(all(str), 'B'), reqb = count(all(str), 'S'), reqc = count(all(str), 'C'), a, b, c, x, y, z;
  ll total = 0, cost, cnt = 0;
  cin >> a >> b >> c >> x >> y >> z >> cost;
  if (reqa == 0)
    a = 0, x = 0;
  if (reqb == 0)
    b = 0, y = 0;
  if (reqc == 0)
    c = 0, z = 0;
  while (a != 0 || b != 0 || c != 0) {
    if (a < reqa) {
      total += (reqa - a) * x;
      a = 0;
    } else {
      a -= reqa;
    }
    if (b < reqb) {
      total += (reqb - b) * y;
      b = 0;
    } else
      b -= reqb;
    if (c < reqc) {
      total += (reqc - c) * z;
      c = 0;
    } else
      c -= reqc;
    if (total > cost) {
      cout << cnt;
      return 0;
    }
    ++cnt;
  }
  cost -= total;
  total = 0;
  ll start = 0, end = cost, mid;
  while (start <= end) {
    mid = start + (end - start) / 2;
    total = (mid * reqa * x) + (mid * reqb * y) + (mid * reqc * z);
    if (total == cost) {
      cnt += mid;
      cout << cnt;
      return 0;
    } else if (total < cost) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
//  total = (max(start, end) * reqa * x) + (max(start, end) * reqb * y) + (max(start, end) * reqc * z);
//  if (total <= cost) {
//    cout << cnt + max(start, end);
//  } else {
//    total = (min(start, end) * reqa * x) + (min(start, end) * reqb * y) + (min(start, end) * reqc * z);
//    if (total <= cost) {
//      cout << cnt + min(start, end);
//    } else
//      cout << cnt;
//  }

//  total = ((start - 1) * reqa * x) + ((start - 1) * reqb * y) + ((start - 1) * reqc * z);
    cout << cnt + max(start - 1, 0LL);
  return 0;
}
