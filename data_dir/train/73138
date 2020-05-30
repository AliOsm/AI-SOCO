#ifndef Local
#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma comment(linker, "/STACK:1024000000,1024000000")
#endif

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

// gp_hash_table<int, int> table;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 2003;
const int MOD = 998244353;

int memo_pre[N][N];
int memo_suf[N][N];
string s;

int dp_pre(int i, int cnt) {
  if (i == -1) {
    return cnt == 0;
  }
  int& res = memo_pre[i][cnt];
  if (res != -1) return res;
  res = 0;
  if (s[i] == '(') {
    res = dp_pre(i - 1, cnt - 1);
  } else if (s[i] == ')') {
    res = dp_pre(i - 1, cnt);
  } else {
    res = dp_pre(i - 1, cnt - 1);
    res = (res + dp_pre(i - 1, cnt)) % MOD;
  }
  return res;
}

int dp_suf(int i, int cnt) {
  cnt = max(cnt , 0);
  if (i == s.size()) return cnt == 0;
  int& res = memo_suf[i][cnt];
  if (res != -1) return res;
  res = 0;
  if (s[i] == '(') {
    res = dp_suf(i + 1, cnt);
  } else if (s[i] == ')') {
    res = dp_suf(i + 1, cnt - 1);
  } else {
    res = dp_suf(i + 1, cnt - 1);
    res = (res + dp_suf(i + 1, cnt)) % MOD;
  }
  return res;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  memset(memo_pre, -1, sizeof memo_pre);
  memset(memo_suf, -1, sizeof memo_suf);

  cin >> s;
  int res = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (s[i] == ')') continue;
    for (int x = 1; x <= i + 1; ++x) {
      int tmp = dp_pre(i - 1, x - 1);
      tmp = 1LL * tmp * dp_suf(i + 1, x) % MOD;
      res = (res + tmp) % MOD;
    }
  }

  cout << res << endl;
}
