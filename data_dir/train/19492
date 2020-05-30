#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/numeric>

using namespace __gnu_pbds;
using namespace __gnu_cxx;
using namespace std;

#define popCnt(x) (__builtin_popcountll(x))

typedef long long Long;

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  int n, m, k;
  cin >> n >> m >> k;

  vector<int> frogs(m), mosqs(k);
  for (int& x : frogs) {
    cin >> x;
  }
  for (int& x : mosqs) {
    cin >> x;
  }

  int res = 101;
  vector <int> vec;


  for (int i = 0 ; i < m ; ++i) {
    int tmp = 0;
    for (int j : mosqs) {
      tmp += (j % frogs[i] == 0);
    }
    if (tmp < res) {
      res = tmp;
      vec.clear();
    }
    if (tmp == res) {
      vec.push_back(i);
    }
  }
  cout << vec.size() << endl;
  for (int x : vec) {
    cout << x + 1 << " ";
  }
}

