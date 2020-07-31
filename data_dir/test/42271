#pragma GCC optimize ("O3")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma comment(linker, "/STACK:1024000000,1024000000")

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define popCnt(x) (__builtin_popcountll(x))
typedef long long Long;

// gp_hash_table<int, int> table;

const int N = 2e5 + 5;

queue<int> pile, tmp_pile;
set<int> in_hand, tmp_in_hand;
int n;

void prep(int x) {
  tmp_pile = pile;
  tmp_in_hand = in_hand;
  tmp_in_hand.erase(0);

  while (x--) {
    if (tmp_in_hand.size() == n) return;
    tmp_pile.push(0);
    int front = tmp_pile.front();
    if (front != 0) {
      tmp_in_hand.insert(front);
    }
    tmp_pile.pop();
  }

}

int validate(int x) {
  prep(x);
  int cnt = 0;
  while (!tmp_in_hand.empty()) {
    int nxt = *tmp_in_hand.begin();
    ++cnt;
    tmp_pile.push(nxt);
    tmp_in_hand.erase(nxt);
    if (tmp_pile.front() != 0) {
      tmp_in_hand.insert(tmp_pile.front());
    }
    tmp_pile.pop();
  }
  for (int i = 1; i <= n; ++i) {
    if (tmp_pile.front() != i) return -1;
    tmp_pile.pop();
  }
  return cnt;
}

int solve() {
  int res_0 = validate(0);
  if (res_0 != -1) {
    return res_0;
  }
  int low = 1, high = n, ans = 2 * n + 7;
  while (low <= high) {
    int mid = (low + high) / 2;
    int res = validate(mid);
    if (res != -1) {
      ans = mid + res;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
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
    int x;
    cin >> x;
    if (x != 0) {
      in_hand.insert(x);
    }
  }

  for (int i = 0; i < n; ++i) {
    int x;
    cin >> x;
    pile.push(x);
  }

  cout << solve() << endl;

}

