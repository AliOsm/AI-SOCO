#define _USE_MATH_DEFINES
#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <complex>
#include <cmath>
#include <numeric>
#include <bitset>
#include <functional>

using namespace std;

#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
  cerr << name << ": " << arg1 << endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << ": " << arg1 << " |";
  __f(comma + 1, args...);
}

typedef long long int64;
typedef pair<int, int> ii;
const int INF = 1 << 29;
const int64 INF64 = 1LL << 60;
const int MOD = 1e9 + 7;

const int N = 1e5 + 10;
int a[N], cnt[N];
int64 sum;

void solve(int L, int R, int low, int high,
           const vector<int64>& d, vector<int64>& e) {
  if (L > R) return;
  int M = (L + R) / 2;
  for (int i = L - 1; i < M; ++i) sum += cnt[a[i]]++;
  int mid = -1;
  e[M] = INF64;
  for (int i = low; i <= high && i < M; ++i) {
    int64 cur = d[i] + sum;
    if (e[M] > cur) {
      e[M] = cur;
      mid = i;
    }
    sum -= --cnt[a[i]];
  }
  for (int i = low; i <= high && i < M; ++i) sum += cnt[a[i]]++;

  for (int i = L - 1; i < M; ++i) sum -= --cnt[a[i]];
  solve(L, M - 1, low, mid, d, e);

  for (int i = L - 1; i < M; ++i) sum += cnt[a[i]]++;
  for (int i = low; i < mid; ++i) sum -= --cnt[a[i]];
  solve(M + 1, R, mid, high, d, e);
  for (int i = L - 1; i < M; ++i) sum -= --cnt[a[i]];
  for (int i = low; i < mid; ++i) sum += cnt[a[i]]++;
}

int main() {
  int n, m;
  scanf("%d%d", &n, &m);
  for (int i = 0; i < n; ++i) {
    scanf("%d", &a[i]);
  }
  vector<int64> d(n + 1), e(n + 1);
  sum = 0;
  for (int i = 1; i <= n; ++i) {
    sum += cnt[a[i - 1]]++;
    d[i] = sum;
  }
  memset(cnt, 0, sizeof(cnt));
  for (int k = 2; k <= m; ++k) {
    sum = 0;
    solve(1, n, 0, n - 1, d, e);
    swap(d, e);
    // trace(k);
    // for (int i = 1; i <= n; ++i) {
    //   trace(i, d[i]);
    // }
  }
  printf("%lld\n", d[n]);
  return 0;
}
