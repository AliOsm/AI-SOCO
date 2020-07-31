#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long
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
const int N = 2e5 + 9, OO = 2e9 + 9;

int main() {
  debug();
  int n, cnt = 0;
  string str;
  cin >> n >> str;
  for (int i = 0; i < (int)str.size(); ++i) {
    if( !(i & 1) ) {
      if(i +1 < n && str[i] == str[i+1]) {
        str.erase(str.begin() + i);
        --i;
        ++cnt;
      }
    }
  }
  if(str.size() & 1) {
    ++cnt;
    str.erase(str.begin() + str.size() - 1);
  }
  cout << cnt << endl;
  cout << str;
}