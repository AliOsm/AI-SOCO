#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(2), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, OO = 1e9;

bool vis[N];

int main() {
  fastIO;
  int n, a, cnt = 0;
  cin >> n;
  vector<int> vec;
  for (int i = 0; i < n; ++i) {
    cin >> a;
    vec.push_back(a);
  }
  sort(all(vec));
  for(int a: vec) {
    if(a > 1 && !vis[a - 1]) {
      vis[a - 1] = 1;
      ++cnt;
    } else if(!vis[a]) {
      vis[a] = 1;
      ++cnt;
    } else if(!vis[a+1]) {
      vis[a + 1] = 1;
      ++cnt;
    }

  }
  cout << cnt;
  return 0;
}
