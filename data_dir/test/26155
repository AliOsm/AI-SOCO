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

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

const int N = 2e5 + 5;

struct Node {
  int start, end; // The node covers the range [start,end].

  Long min_cost = 0;
  Long lazy = 0;

  static Node merge(const Node& a, const Node& b) {
    Node res;
    res.start = a.start;
    res.end = b.end;

    res.min_cost = min(a.min_cost + a.lazy, b.min_cost + b.lazy);

    return res;
  }

  bool inRange(int x) const {
    return start <= x && x <= end;
  }

  void print() const {
    cout << start << " " << end << " " << min_cost << " " << lazy << endl;
  }
};

struct SegmentTree {
  static const int kSize = 1 << int(log2(N) + 2);

  array<Node, kSize> nodes;

  void build(int node_id, int left, int right, const vector<Long>& costs) {
    Node& node = nodes[node_id];
    node.lazy = 0;
    node.start = left, node.end = right;
    if (left == right) {
      node.min_cost = costs[left];
      return;
    }

    int mid = (left + right) / 2;
    build(node_id * 2, left, mid, costs);
    build(node_id * 2 + 1, mid + 1, right, costs);
    node = Node::merge(nodes[node_id * 2], nodes[node_id * 2 + 1]);
  }

  void build(const vector<Long>& costs) {
    build(1, 0, costs.size() - 1, costs);
  }

  void push(int node_id) {
    auto& node = nodes[node_id];
    node.min_cost += node.lazy;
    if (node.start != node.end) {
      nodes[node_id * 2].lazy += node.lazy;
      nodes[node_id * 2 + 1].lazy += node.lazy;
    }
    node.lazy = 0;
  }

  void update(int node_id, int l, int r, Long val) {
    if (r < l) return;
    push(node_id);
    auto& node = nodes[node_id];
    if (node.start > r || node.end < l) return;
    if (l <= node.start && node.end <= r) {
      node.lazy += val;
      push(node_id);
      return;
    }
    update(node_id * 2, l, r, val);
    update(node_id * 2 + 1, l, r, val);
    node = Node::merge(nodes[node_id * 2], nodes[node_id * 2 + 1]);
  }

  Long query() {
    return nodes[1].min_cost + nodes[1].lazy;
  }

} seg_tree;

Long cost_val[N];
Long cost_ind[N];

int perm[N];
int pos[N];
int n;

void buildPos() {
  for (int i = 0; i < n; ++i) {
    pos[perm[i]] = i;
  }
}

Long solve() {
  buildPos();
  vector<Long> costs;
  for (int i = 0; i < n - 1; ++i) {
    costs.emplace_back(cost_ind[i]);
    if (i != 0) {
      costs.back() += costs[i - 1];
    }
  }
  seg_tree.build(costs);
  Long res = seg_tree.query();
  for (int i = 1; i <= n; ++i) {
    seg_tree.update(1, 0, pos[i] - 1, cost_val[i]);
    seg_tree.update(1, pos[i], n - 2, -cost_val[i]);
    res = min(res, seg_tree.query());
  }
  return res;
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
    cin >> perm[i];
  }

  for (int i = 0; i < n; ++i) {
    cin >> cost_ind[i];
    cost_val[perm[i]] = cost_ind[i];
  }

  Long res = solve();

  cout << solve() << endl;

}
