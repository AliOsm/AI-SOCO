#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 200005;

pair<int, int> bids[N];
int n;

bool exc[N];
int prev_[N];
int query[N];

set<int> pos[N];

int Solve() {
  int curr = n - 1;
  while (exc[bids[curr].first]) {
    curr = prev_[curr];
  }
  return curr;
}

void BuildPrev() {
  unordered_set<int> st;

  int curr = n - 1;
  for (int i = n - 1; i > 0; --i) {
    if (curr == i) {
      --curr;
    }
    st.insert(bids[i].first);
    while (st.count(bids[curr].first) > 0) {
      --curr;
    }
    prev_[i] = curr;
  }

}

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
//  freopen("o.txt", "wt", stdout);
#endif

  cin >> n;
  ++n;
  bids[0] = {0,0};
  for (int i = 1; i < n; ++i) {
    cin >> bids[i].first >> bids[i].second;
    pos[bids[i].first].insert(i);
  }

  BuildPrev();

  int q;
  cin >> q;
  while (q--) {
    int k;
    cin >> k;

    for (int i = 0; i < k; ++i) {
      cin >> query[i];
      exc[query[i]] = true;
    }

    int bidder = Solve();
    if (bidder != 0) {
      query[k++] = bids[bidder].first;
      exc[bids[bidder].first] = true;
    }
    int bid = Solve();
    int ans = *pos[bids[bidder].first].lower_bound(bid);

    cout << bids[ans].first << ' ' << bids[ans].second << '\n';

    for (int i = 0; i < k; ++i) {
      exc[query[i]] = false;
    }

  }

  return 0;
}
