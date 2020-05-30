#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = pair<int,int>;

#define fi first
#define se second
#define eb emplace_back
#define all(x) x.begin(), x.end()

int const N = 100 * 1000 + 16;
int const M = 1000 * 1000 * 1000 + 7;



int main() {
  cin.tie(0);
  cin.sync_with_stdio(0);

  string s;
  cin >> s;

  int n;
  cin >> n;
  vector<string> a(n);
  for(int i = 0; i < n; ++i) {
    cin >> a[i];
  }

  bool can = false;
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < n; ++j) {
      string m = a[i] + a[j];
      if(m.find(s) != string::npos) {
        can = true;
        break;
      }
    }
  }

  cout << (can ? "YES" : "NO");
}