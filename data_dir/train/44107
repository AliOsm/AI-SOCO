#include <bits/stdc++.h>
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;
typedef unsigned long long ULong;

const int N = 5e5 + 5;

Long arr[N];
Long neg_arr[N];
Long sum[N];
Long diff[N][2];
int n;

int count_greater_than_k(int ind, int k) {
  return (lower_bound(neg_arr + ind, neg_arr + n, -k) - neg_arr) - ind;
}

Long getDiff(int ind, bool b) {
  Long res = 0;
  for (int i = 1; i <= ind; ++i) {
    res += arr[i - 1];
  }
  if (b) {
    res -= ind * (ind + 1);
  } else {
    res -= ind * (ind - 1);
  }
  for (int i = ind + 1; i <= n; ++i) {
    res -= min(1LL * (b ? ind + 1 : ind), arr[i - 1]);
  }
  return res;
}

void build() {
  sort(arr, arr + n, greater<int>());
  for (int i = 1; i <= n; ++i) {
    neg_arr[i - 1] = -arr[i - 1];
    diff[i][0] = diff[i - 1][0] + arr[i - 1];
    diff[i][1] = diff[i][0];
    sum[i] = sum[i - 1] + arr[i - 1];
  }

  for (int i = 1; i <= n; ++i) {
    diff[i][0] -= 1LL * i * (i - 1);
    diff[i][1] -= 1LL * (i + 1) * i;
  }

  for (int i = 1; i <= n; ++i) {
    Long cnt_k = count_greater_than_k(i, i);
    diff[i][0] -= cnt_k * i + sum[n] - sum[i + cnt_k];
//    assert(diff[i][0] == getDiff(i, false));
  }

  for (int i = 1; i <= n; ++i) {
    Long cnt_k = count_greater_than_k(i, i + 1);
    diff[i][1] -= cnt_k * (i + 1) + sum[n] - sum[i + cnt_k];
//    assert(diff[i][1] == getDiff(i, true));
  }

  for (int i = 1; i <= n; ++i) {
    if (diff[i][0] > i) {
      diff[i][0] = N;
    }
  }

  for (int i = 2; i <= n; ++i) {
    diff[i][0] = max(diff[i][0], diff[i - 1][0]);
  }

  for (int i = n - 1; i >= 1; --i) {
    diff[i][1] = max(diff[i][1], diff[i + 1][1]);
  }
  diff[n + 1][0] = diff[n + 1][1] = diff[0][0] = diff[0][1] = -N;
}

int getPos(int x) {
  return lower_bound(neg_arr, neg_arr + n, -x) - neg_arr;
}

bool valid(int ind, int x) {
  Long d = sum[ind - 1] + x;
  d -= 1LL * ind * (ind - 1);
  Long cnt_k = count_greater_than_k(ind - 1, ind);
  d -= cnt_k * ind + sum[n] - sum[ind - 1 + cnt_k];
  return d <= 0;
}

bool can(int x) {
  int pos = getPos(x) + 1;
  if (!valid(pos, x)) return false;
  if (diff[pos - 1][0] - x > 0) return false;
  if (x + diff[pos][1] > 0) return false;
  return true;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
#else
#define endl '\n'
#endif

  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
  }

  build();

  bool found = false;
  bool even = (~sum[n] & 1);

  for (int x = !even; x <= n; x += 2) {
    if (can(x)) {
      cout << x << " ";
      found = true;
    }
  }

  if (!found) {
    cout << -1;
  }

}
