#pragma comment(linker,"/STACK:100000000000,100000000000")

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <stack>
#include <set>
#include <iomanip>
#include <queue>
#include <map>
#include <functional>
#include <list>
#include <sstream>
#include <ctime>
#include <climits>
#include <bitset>
#include <list>
#include <cassert>
#include <complex>

using namespace std;

/* Constants begin */
const long long inf = 2e18 + 7;
const long long mod = 1e9+9;
const double eps = 1e-9;
const double PI = 2*acos(0.0);
const double E = 2.71828;
/* Constants end */

/* Defines begin */
#define pb push_back
#define mp make_pair
#define ll long long
#define double long double
#define F first
#define S second
#define all(a) (a).begin(),(a).end()
#define forn(i,n) for (int (i)=0; (i)<(n); ++(i))
#define random (rand()<<16|rand())
#define sqr(x) (x)*(x)
#define base complex<double>
/* Defines end */

int n, m;

int x[300005], y[300005];

int cnt[300005];

vector<int> g[300005];

int a[300005];

int main(void){
  #ifdef nobik
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
  #endif
  scanf("%d %d", &n, &m);
  forn(i, n) g[i].reserve(32);
  forn(i, n){
    scanf("%d %d", x + i, y + i); --x[i]; --y[i];
    if(x[i] > y[i]) swap(x[i], y[i]);
    g[x[i]].pb(y[i]);
    g[y[i]].pb(x[i]);
    ++cnt[x[i]];
    ++cnt[y[i]];
  }
  ll res = 0;
  forn(i, n) a[i] = cnt[i];
  sort(a, a + n);
  forn(i, n){
    int from = lower_bound(a, a + n, m - cnt[i]) - a;
    res += n - from;
    if(from < n && a[from] <= cnt[i]) --res;
    forn(j, g[i].size()){
      int to = g[i][j];
      if(cnt[i] + cnt[to] == m){
        --res;
      }
      --cnt[to];
    }
    forn(j, g[i].size()){
      int to = g[i][j];
      ++cnt[to];
    }
  }
  printf("%I64d\n", res / 2);
  return 0;
}

