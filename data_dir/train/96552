#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-15, PI = acos(-1);
const int N = 2e5 + 9, OO = 1e9;

int arr[N];
vector<int> idx;

int main() {
  fastIO;
  // freopen("input.in", "rt", stdin);//  freopen("output.in", "wt", stdout);
  int q;
  cin >> q;
  while(q--) {
    int n, m;
    idx.clear();
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      cin >> arr[i];
      if(arr[i] & 1)
        idx.push_back(i);
    }
    if((m % 2) != ((int)idx.size() % 2) || ((int)idx.size() < m)) {
      cout << "NO\n";
      continue;
    }
    cout << "YES\n";
    int fin = (int)idx.size() - m;
    for (int i = fin; i < (int)idx.size() - 1; ++i) {
      cout << idx[i] + 1 << ' ';
    }
    cout << n;
    cout << '\n';
  }
  return 0;
}
