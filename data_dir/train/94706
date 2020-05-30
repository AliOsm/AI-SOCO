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

bool primes[N];
vector<int> vec, ans;

void sieve() {
  primes[0] = primes[1] = 1;
  int mx = 1e5 + 1;
  for (ll i = 2; i * i <= mx; ++i) {
    if(!primes[i]) {
      for (ll j = i * i; j < mx; j += i)
        primes[j] = 1;
    }
  }
  for (int i = 0; i < mx; ++i) {
    if(!primes[i])
      vec.push_back(i);
  }
}

int main() {
  sieve();
  debug();
  ll n, cur = 1;
  cin >> n;
  ans = vector<int>(n);
  for (ll i = 2; i <= n; ++i) {
    if(primes[i]) continue;
    ans[i-1] = cur;
    for (ll j = i * i; j <= n; j += i)
      ans[j-1] = cur;
    ++cur;
  }
  for (int i = 1; i < n; ++i)
    cout << ans[i] << " ";
  return 0;
}