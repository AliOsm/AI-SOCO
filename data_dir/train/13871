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

vector<int> solve(vector<int> cnt, vector<int> res) {
  for (int i = 0; i <= 3; ++i) {
    while (cnt[i] > 0) {
      if (abs(res.back() - i) > 1) return res;
      if (res.back() == i) {
        if (cnt[i + 1] == 0) {
          return res;
        }
        --cnt[i + 1];
        res.push_back(i + 1);
      }
      --cnt[i];
      res.push_back(i);
    }
  }
  return res;
}

const int N = 5;
int cnt[N];

bool valid(const vector<int>& res) {
  for (int i = 0; i < 4; ++i) {
    if (count(res.begin(), res.end(), i) != cnt[i]) return false;
  }
  return true;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  for (int i = 0; i < 4; ++i) {
    cin >> cnt[i];
  }

  for (int i = 0; i < 4; ++i) {
    if (cnt[i] == 0) continue;
    if (i > 1 && cnt[0] != 0) break;
    if (i == 3 && cnt[1] != 0) break;
    vector<int> res;
    res.push_back(i);
    vector<int> tmp_cnt(cnt, cnt + N);
    --tmp_cnt[i];
    res = solve(tmp_cnt, res);
    if (valid(res)) {
      cout << "YES" << endl;
      for (int x : res) {
        cout << x << " ";
      }
      cout << endl;
      return 0;
    }
  }

  cout << "NO" << endl;

}
