#include <bits/stdc++.h>
//#include <ext/pb_ds/tree_policy.hpp>
//#include <ext/pb_ds/assoc_container.hpp>
using namespace std;
//using namespace __gnu_pbds;
//template<typename key, typename val>
//using ordered_tree =
//  tree<key, val, greater<>, rb_tree_tag, tree_order_statistics_node_update>;
typedef long long int64;
typedef complex<double> comp;
const double pi = 3.14159265358979323846;
const int inf = (int)1e+9 + 2;
const int64 inf64 = (int64)1e+18 + 2;
const double dinf = 1e+20;
const int mod = 1'000'000'007;//*/998244353;
const int base = 2187;
const double eps = 1e-8;
const int N = 100'000;
const int LOGN = 19;

int n, m, k;

struct Matrix {
  Matrix operator*(const Matrix& m) const {
    Matrix res;
    memset(res.a, 0, sizeof(a));
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        for (int q = 0; q < 3; ++q) {
          res.a[i][j] += a[i][q] * m.a[q][j];
          res.a[i][j] %= mod - 1;
        }
      }
    }
    return res;
  }

  void Identity() {
    memset(a, 0, sizeof(a));
    a[0][0] = 1;
    a[1][1] = 1;
    a[2][2] = 1;
  }

  int64 a[3][3] = {{0, 0, 1}, {1, 0, 1}, {0, 1, 1}};
};

int64 pw(int64 a, int64 b) {
  int64 res = 1;
  while (b) {
    if (b & 1) {
      res *= a;
      res %= mod;
    }
    a *= a;
    a %= mod;
    b >>= 1;
  }
  return res;
}

Matrix pw(Matrix a, int64 b) {
  Matrix res;
  res.Identity();
  while (b) {
    if (b & 1) {
      res = res * a;
    }
    a = a * a;
    b >>= 1;
  }
  return res;
}

void solve(int test) {
  int f1, f2, f3, c;
  int64 n;
  cin >> n >> f1 >> f2 >> f3 >> c;

  set<int> st;
  map<int, int> mp1, mp2, mp3;
  auto fn = [&] (int f, map<int, int>& mp, int add = 1) {
    for (int i = 2; i * i <= f; ++i) {
      if (f % i == 0) {
        st.insert(i);
      }
      for (; f % i == 0; f /= i) {
        mp[i] += add;
      }
    }
    if (f != 1) {
      st.insert(f);
      mp[f] += add;
    }
  };
  fn(f1, mp1);
  fn(f2, mp2);
  fn(f3, mp3);
  fn(c, mp1, 1);
  fn(c, mp2, 2);
  fn(c, mp3, 3);

  Matrix a = pw(Matrix(), n - 3);
  int64 ans = 1;
  for (int p : st) {
    int64 x = mp1[p] * a.a[0][2] + mp2[p] * a.a[1][2] + mp3[p] * a.a[2][2];
    ans *= pw(p, x);
    ans %= mod;
  }
  cout << ans * pw(pw(c, n), mod - 2) % mod << '\n';
}

void precalc() {
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0), cout.tie(0);
  precalc();
  int test = 1;
  //cin >> test;
  //auto start = chrono::high_resolution_clock::now();
  for (int i = 1; i <= test; ++i) {
    solve(i);
  }
  //cerr << chrono::duration_cast<chrono::milliseconds>(chrono::high_resolution_clock::now() - start).count() << '\n';
  return 0;
}
