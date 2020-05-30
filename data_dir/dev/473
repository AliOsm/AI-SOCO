
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int const N = 200 * 1000 + 16;
int const M = 1000*1000*1000 + 7;

int main() {
  srand(time(0));
  cin.tie(0);
  cin.sync_with_stdio(0);

  int n;
  static int a[3010];
  
  cin >> n;
  for(int i = 0; i < n; ++i)
    cin >> a[i];

  int ans = 0;
  sort(a, a+n);
  int last = 0;
  for(int i = 0; i < n; ++i) {
    if(last < a[i]) {
      last = a[i];
    } else {
      last++;
      ans += last-a[i];
    }
  }
  cout << ans << endl;
}