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
#define N 502
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
int n;
int main() {
  scanf("%d", &n);
  vector<ll> rk;
  rk.clear();
  ll ans=0LL;
  for (int i = 1; i <= n; ++i) {
    ll a,b;
    scanf("%lld%lld", &a, &b);
    rk.push_back(a-b);
    ans -= a;
    ans += n*b;
  }
  sort(rk.begin(), rk.end());
  reverse(rk.begin(), rk.end());
  for (int i = 0; i < rk.size(); ++i) {
    ans += (i+1)*rk[i];
  }
  cout<<ans<<endl;
  return 0;
}
