#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int N = 200005;

struct Node {
  ll weight;
  ll strength;
  ll sum = 0;
  ll shortage = 0;
} nodes[N];

vector<int> children[N];

int n;

ll GetSum(int node_id, bool& can) {
  Node& node = nodes[node_id];
  node.sum = 0;
  node.shortage = 0;
  for (int child : children[node_id]) {
    node.sum += GetSum(child, can);
    node.shortage += nodes[child].shortage;
  }
  node.shortage = max(node.shortage, node.sum - node.strength);
  if (node_id != 1) {
    can &= (node.sum <= node.strength);
  }
  return node.sum + node.weight;
}

ll Fix(int node_id, ll shortage) {
  shortage = max(shortage, 0LL);
  ll dec = 0;
  Node& node = nodes[node_id];
  shortage += node.shortage;

  for (int child : children[node_id]) {
    shortage -= nodes[child].shortage;
    shortage = max(shortage, 0LL);
  }

  for (int child : children[node_id]) {
    ll child_shortage = nodes[child].shortage;
    ll tmp = Fix(child, shortage) - child_shortage;
    dec += tmp + child_shortage;
    shortage -= tmp;
    shortage = max(shortage, 0LL);
  }

  if (node_id != 1) {
    node.sum -= dec;
    ll node_dec = min(node.strength, node.weight - 1);
    node_dec = min(node_dec, shortage);
    node_dec = min(node_dec, node.strength - node.sum);
    node_dec = max(node_dec, 0LL);
    node.strength -= node_dec;
    node.weight -= node_dec;
    dec += node_dec;
  }
  return dec;
}

pair<int, int> edges[N];

void Print() {
  cout << n << '\n';
  for (int i = 1; i < n; ++i) {
    Node& node = nodes[edges[i].second];
    cout << edges[i].first << ' ' << edges[i].second << ' ' << node.weight
      << ' ' << node.strength << '\n';
  }
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
  freopen("test.in", "r", stdin);
  freopen("wa.txt", "w", stdout);
#endif

  cin >> n;

  for (int i = 1; i < n; ++i) {
    int x, y, w, p;
    cin >> x >> y >> w >> p;

    children[x].push_back(y);
    nodes[y].weight = w;
    nodes[y].strength = p;

    edges[i] = {x,y};
  }

  nodes[1].strength = 1e16;
  nodes[1].weight = 1;

  bool can = true;
  GetSum(1, can);
  Fix(1, 0);

  can = true;
  GetSum(1, can);

  if (!can) {
    cout << -1;
    return 0;
  }

  Print();

}
