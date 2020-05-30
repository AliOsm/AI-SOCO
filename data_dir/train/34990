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
const int N = 1e5 + 9, OO = 1e9 + 9;

ll n, k;
ll steps = 0;
void doIt() {
  if (n % k == 0)
    n /= k, ++steps;
  else {
    steps += n % k;
    n -= (n % k);
  }
}

int main() {
  debug();
  int t;
  cin >> t;
  while (t--) {
    cin >> n >> k;
    steps = 0;
    while(n != 0) {
      doIt();
    }
    cout << steps << endl;
  }
  return 0;
}