#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define all(v)    ((v).begin()),((v).end())
#define clr(a,b)  memset(a,b,sizeof(a))
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
// freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}

int const N = 2e5 + 9, OO = 1e9;

ll arr[N];
vector<ll> vec;

int main() {
  debug();
  ll n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }
  ll mn = *min_element(arr, arr+n);
  for (int i = 0; i < n; ++i) {
    if(arr[i] == mn)
      vec.push_back(i);
  }
  ll mx = 0;
  for (int i = 0; i < (int)vec.size(); ++i) {
    if(i + 1 == (int)vec.size()) {
      mx = max(mx, n - (vec[i] - vec[0] + 1));
    } else {
      mx = max(mx, vec[i+1] - vec[i] - 1);
    }
  }
  ll res = (ll)mx + (ll)n * (ll)mn;
  cout << res;
  return 0;
}
