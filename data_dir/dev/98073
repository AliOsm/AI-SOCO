#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin);
#define write freopen("output.in", "wt", stdout);
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
double const EPS = 1e-8, PI = acos(-1);
const int N = 2e5 + 9, M = 50, OO = 1e9 + 9, MOD = 1e9 + 7;

int main() {
  fastIO
  int n;
  string strA, strB;
  cin >> n >> strA >> strB;
  string res = "abc";
  vector<string> vec;
  do {
    string firstStr, secStr;
    for (int i = 0; i < n; ++i)
      firstStr += res;
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < n; ++j)
        secStr += res[i];
    }
    vec.push_back(firstStr);
    vec.push_back(secStr);
  } while(next_permutation(all(res)));

  for(string it: vec) {
    if(it.find(strA) == -1 && it.find(strB) == -1) {
      cout << "YES\n";
      cout << it;
      return 0;
    }
  }
  cout << "NO";
  return 0;
}
