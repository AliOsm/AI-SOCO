#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);  //freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(6);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}
double const EPS = 1e-9, PI = acos(-1);
int const N = 2e5 + 9, M = 1e5 + 9, OO = 1e9;

int arr[N];
multiset<int> stA, stB;

int main() {
  debug();
  int n, z;
  cin >> n >> z;
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }
  sort(arr, arr+n);
  for (int i = 0; i < n/2; ++i) {
    stA.insert(arr[i]);
  }
  for (int i = n/2; i < n; ++i) {
    stB.insert(arr[i]);
  }
  int total = 0;
  for (int i = 0; i < n/2; ++i) {
    int x = *stA.begin();
    auto y = stB.lower_bound(x + z);
    if(y == stB.end())
      break;
    ++total;
    stA.erase(stA.begin());
    stB.erase(y);
  }
  cout << total;
}
