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

const int N = 2e5 + 5;

int n, q;

deque<int> dq;

pair<int, int> res[N];
int curr_mx = 0;
int cycle_start = 0;

pair<int, int> solve(Long x) {
  if (x < cycle_start) {
    return res[x];
  }
  return res[cycle_start + (x - cycle_start) % (n - 1)];
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  cin >> n >> q;

  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    dq.push_front(x);
  }

  for (int i = 1; i < N; ++i) {
    res[i].first = dq.back();
    dq.pop_back();
    res[i].second = dq.back();
    dq.pop_back();
    if (res[i].first != curr_mx) {
      curr_mx = res[i].first;
      cycle_start = i;
    }
    dq.push_front(min(res[i].first, res[i].second));
    dq.push_back(max(res[i].first, res[i].second));
  }

  while (q--) {
    Long x;
    cin >> x;
    auto res = solve(x);
    cout << res.first << " " << res.second << endl;
  }

}
