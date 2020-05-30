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

int a, b;
vector<pair<int, pair<int, int>>> vec;

int main() {
  debug();
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> a >> b;
    vec.push_back({a - b, {a, b}});
  }
  sort(vec.rbegin(), vec.rend());

  ll total = 0;
  for (int i = 0; i < n; ++i) {
    total += ((ll)vec[i].second.first * i) + ((ll)vec[i].second.second * (n-i-1));
  }
  cout << total;
  return 0;
}
