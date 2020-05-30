#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;


int main() {
  fastIO;
  int A = 0, B = 0, n, k, ptr1 = 0, ptr2 = 0, mxAns = 0;
  string str;
  cin >> n >> k;
  cin >> str;
  bool noInc = 0;
  while(ptr1 < n && ptr2 < n) {
    if( !noInc && str[ptr2] == 'a')
      ++A;
    else if(!noInc)
      ++B;
    if(min(A, B) > k) {
      if(str[ptr1] == 'a')
        --A;
      else
        --B;
      ++ptr1;
      noInc = 1;
      continue;
    }
    mxAns = max(mxAns, ptr2 - ptr1 + 1);
    ++ptr2;
    noInc = 0;
  }
  cout << mxAns;
  return 0;
}
