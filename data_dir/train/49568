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

const int N = 3e5 + 5;

int n;
int k;

Long acc[N];

int main(int argc, char *argv[]) {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  multiset<Long> st;

  cin >> n >> k;
  for (int i = 1; i <= n; ++i) {
    cin >> acc[i];
    acc[i] += acc[i - 1];
    if (i != n) {
      st.insert(acc[i]);
    }
  }

  while (st.size() > k - 1) {
    st.erase(st.find(*st.rbegin()));
  }

  Long sum = k * acc[n];

  for (Long x : st) {
    sum -= x;
  }

  cout << sum << endl;

}

