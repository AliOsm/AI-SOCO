#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
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

  int n;
  cin >> n;

  vector<int> vec(n);
  for (int& x : vec) {
    cin >> x;
  }

  sort(vec.begin(), vec.end());

  for (int i = 0; i < vec.size(); i += 2) {
    cout << vec[i] << " ";
  }

  for (int i = int(vec.size()) - 1 -  (vec.size() & 1) ; i >= 0 ; i -= 2) {
    cout << vec[i] << " ";
  }

}
