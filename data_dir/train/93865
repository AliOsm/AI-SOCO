#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define fastIO cout << fixed << setprecision(3), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
double const EPS = 1e-15, PI = acos(-1);
const int N = 1e5 + 9, OO = 1e5;

ll arr[N], elm[N];

int main() {
  fastIO;
  int n, k;
  cin >> n >> k;
  for (int i = 1; i <= n; ++i)
    cin >> arr[i];
  sort(arr + 1, arr + n + 1);
  for (int i = 1; i <= n; ++i)
    elm[i] = arr[i];
  for (int i = 1; i <= n; ++i)
    arr[i] += arr[i-1];
  int num, ans = 0, cnt = 0;
  for (int i = n; i > 0; --i) {
    cnt = 1;
    int start = 1, end = i, mid;
    while(start <= end) {
      mid = start + (end - start) / 2;
      if((elm[i] * mid) - (arr[i] - arr[i - mid]) <= k) {
        cnt = max(cnt, mid);
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
    if(cnt >= ans)
      num = elm[i], ans = cnt;
  }
  cout << ans << ' ' << num;
  return 0;
}
