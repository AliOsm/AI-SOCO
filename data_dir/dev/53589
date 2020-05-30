#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 300005;
const int kMax = 1e9;
template<class T>
struct BIT {
  vector<T> v;
  BIT(int s) {
    Resize(s);
  }
  BIT() {
  }
  void Resize(int s) {
    s = 1 << (int) ceil(log(1.0 * s) / log(2.) + 1e-9);
    v.resize(s);
  }
  T Get(int i) {
    i++;
    T r = 0;
    while (i) {
      r += v[i - 1];
      i -= i & -i;
    }
    return r;
  }
  void Add(int i, T val = 1) {
    i++;
    while (i <= (int) v.size()) {
      v[i - 1] += val;
      i += i & -i;
    }
  }
  int Find(T val) {
    // Find element at index val.
    int s = 0;
    int m = v.size() >> 1;
    while (m) {
      if (v[s + m - 1] < val) val -= v[(s += m) - 1];
      m >>= 1;
    }
    return s;
  }
};

map<int, int> compressed;
map<int, int> uncompressed;

pair<int, int> coupons[N];
multiset<pair<int, int>> sorted_coupons;

void Compress() {
  int ind = 0;
  for (auto& x : compressed) {
    x.second = ind;
    uncompressed[ind] = x.first;
    ++ind;
  }
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
//  freopen("wa.txt", "w", stdout);
#endif

  int n, k;
  cin >> n >> k;

  for (int i = 0; i < n; ++i) {
    cin >> coupons[i].first >> coupons[i].second;
    compressed[coupons[i].second];
    sorted_coupons.emplace(coupons[i].first, coupons[i].second);
  }

  Compress();

  BIT<int> bit(N);

  pair<int, int> max_range = { -kMax - 1, -kMax - 2 };

  int size = 0;

  for (auto& coupon : sorted_coupons) {
    ++size;
    bit.Add(compressed[coupon.second]);
    if (size < k) {
      continue;
    }
    int max_end = uncompressed[bit.Find(size - k + 1)];
    if (max_end - coupon.first > max_range.second - max_range.first) {
      max_range = {coupon.first , max_end};
    }
  }

  cout << max_range.second - max_range.first + 1 << '\n';

  if (max_range.first == -kMax - 1) {
    for (int i = 1; i <= k; ++i) {
      cout << i << ' ';
    }
    return 0;
  }



  for (int i = 0; i < n && k > 0; ++i) {
    if (coupons[i].first <= max_range.first
      && max_range.second <= coupons[i].second) {
      cout << i + 1 << ' ';
      --k;
    }
  }

}
