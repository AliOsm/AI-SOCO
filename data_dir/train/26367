#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef unsigned long long ULong;

const int N = 1e5 + 5;
const int MOD = round(1e9 + 7);

int memo[N];

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  string s;
  cin >> s;
  int last_b = N - 1;

  for (int i = s.size() - 1; i >= 0; --i) {
    memo[i] = memo[i + 1];
    if (s[i] == 'a') {
      memo[i] = (memo[i] + memo[last_b]) % MOD;
      memo[i] = (memo[i] + 1) % MOD;
    }
    if (s[i] == 'b') {
      last_b = i;
    }
  }

  cout << memo[0] << endl;

}
