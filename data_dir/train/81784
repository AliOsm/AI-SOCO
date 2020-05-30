#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
#define readIn freopen("input.in", "rt", stdin);
#define writeOut freopen("output.in", "wt", stdout);
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e5 + 9, M = 4e4 + 9, OO = 1e9;

int a[N], b[N], n;
ll mem[N][3];

ll DP(int x, int c) {
  if(x > n)
    return 0;
  ll& ret = mem[x][c];
  if(~ret)
    return ret;
  ret = 0;
  if(c != 1)
    ret = max(ret, DP(x+1, 1) + a[x]);
  if(c != 2)
    ret = max(ret, DP(x+1, 2) + b[x]);
  ret = max(ret, DP(x+1, 0));
  return ret;
}

int main() {
  fastIO;
  cin >> n;
  for (int i = 0; i < n; ++i)
    cin >> a[i];
  for (int i = 0; i < n; ++i)
    cin >> b[i];
  clr(mem, -1);
  cout << DP(0, 0);
  return 0;
}
