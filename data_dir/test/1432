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

const int N = 1e6 + 7;
const int OO = 1e7;

int count(int x, int y, bool mistakes) {
  if (x == 0 || y == 0) return OO;
  if (y == 1) {
    if (mistakes) return max(0, x - 2);
    return x;
  }

  int res = x / y - mistakes + count(y, x % y, mistakes);
  return res;
}

string build(int x, int y) {
  if (x == 0 || y == 0) return "";
  if (x >= y) return build(x - y, y) + "T";
  return build(x, y - x) + "B";
}

int n, r;

void validate(const string& s, int res) {
  assert(s[0] == 'T');
  assert(s.size() == n);
  int x = 0, y = 1;
  for (char c : s) {
    if (c == 'T') {
      x += y;
    } else {
      y += x;
    }
  }
  assert(max(x, y) == r);
  for (int i = 0; i + 1 < n; ++i) {
    res -= (s[i] == s[i + 1]);
  }
  assert(res == 0);
}

bool solve() {
  int best = -1;
  int res = OO;

  for (int i = 1; i < r; ++i) {
    if (count(r, i, false) == n) {
      int mistakes = count(r, i, true);
      if (mistakes < res) {
        res = mistakes;
        best = i;
      }
    }
  }

  if (best == -1) return false;

  cout << res << endl;
  string s = build(r, best);
  if (s.size() > 1 && s[1] == 'T') {
    s[0] = 'B';
    for (char& c : s) {
      c ^= 'B' ^ 'T';
    }
  }
  cout << s << endl;

  validate(s, res);
  return true;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  cin >> n >> r;
  if (n == 1 && r == 1) {
    cout << 0 << endl;
    cout << "T" << endl;
    return 0;
  }
  if (!solve()) {
    cout << "IMPOSSIBLE" << endl;
    return 0;
  }
}

