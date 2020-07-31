#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#define N 200005
using namespace std;
typedef long long ll;
const ll mod = 998244353LL;
int q;
ll a,b,m;
int main() {
  cin>>q;
  for (int cas=1; cas <= q; ++cas) {
    scanf("%lld%lld%lld", &a, &b, &m);
    if (a==b) {
      cout<<1<<" "<<a<<endl;
      continue;
    } else if (b-a>=1 && b-a<=m) {
      cout<<2<<" "<<a<<" "<<b<<endl;
      continue;
    }
    int k;
    vector<ll> res;
    for (k = 3; k <= 50; ++k) {
      vector<ll> ans(k-1, 0);
      ll b2 = b;
      if (b2/a < (1LL<<(k-2))) continue;
      b2 -= (1LL<<(k-2))*a;
      for (int k2 = k-3; k2 >= 0; --k2) {
        b2 -= (1LL << k2);
        ans[k-3-k2]++;
        if (b2 < 0) break;
      }
      if (b2 < 0) continue;
      b2--;
      ans[k-2]++;
      if (b2 < 0) continue;
      if (b2 <= m-1) {
        ans[k-2] += b2;
        res = ans;
        break;
      }
      ans[k-2] += m-1;
      b2 -= m-1;
      int k2;
      for (k2 = k-3; k2 >= 0; --k2) {
        if (b2 / (1LL<<k2) == 0) continue;
        ll x = min(b2/(1LL<<k2), m-1);
        ans[k-3-k2] += x;
        b2 -= (1LL<<k2)*x;
      }
      if (k2 >= 0) continue;
      if (b2) continue;
      res = ans;
      break;
    }
    if (k > 50) cout<<-1<<endl;
    else {
      printf("%d %lld", k, a);
      ll pre=a;
      for (int i = 0; i < res.size(); ++i) {
        printf(" %lld", pre+res[i]);
        pre += pre+res[i];
      }
      cout<<endl;
    }
  }
  return 0;
}
