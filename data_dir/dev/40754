#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define clr(a,b) memset(a,b,sizeof(a))
#define all(v) ((v).begin()),((v).end())
#define read freopen("input.in", "rt", stdin)
#define write freopen("output.in", "wt", stdout)
#define fastIO cout << fixed << setprecision(0), ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr)
double const EPS = 1e-8, PI = acos(-1);
const int N = 1e6 + 9, M = 3e4 + 9, OO = 1e9 + 1, MOD = 1e9 + 7;
const ll inf = 1e18;

int arr[N], tree[4*N];

int query(int node, int start, int end, int l, int r) {
  if(start > r || end < l || start > end)
    return 0;
  if(start >= l && end <= r)
    return tree[node];
  int mid = (start + end) / 2;
  int p1 = query(node * 2, start, mid, l, r),
      p2 = query(node * 2 + 1, mid + 1, end, l, r);
  return (p1 + p2);
}

void update(int node, int start, int end, int idx) {
  if(start == idx && end == idx) {
    ++tree[node];
    return;
  }
  int mid = (start + end) / 2;
  if(idx <= mid)
    update(node * 2, start ,mid, idx);
  else
    update(node * 2 + 1, mid + 1, end, idx);
  tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

map<int, int> mp;
set<int> st;

int main() {
  fastIO;
  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cin >> arr[i];
    st.insert(arr[i]);
  }
  int idx = 1;
  for(int it: st)
    mp[it] = idx++;
  unsigned ll sum = 0;
  for (int i = 0; i < n; ++i) {
    int val = mp[arr[i]];
    int la = query(1, 1, n, val, n);
    int sm = (val-1) - (i - la);
    sum += (ll)la * sm;
    update(1, 1, n, val);
  }
  cout << sum << endl;
  return 0;
}
