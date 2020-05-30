/*

Our shadows stretch out on the pavement
As I walk in the twilight with you
If we could be together like this forever
Holding hands
It's almost enough to make me cry

The wind grows colder
I can smell winter
Soon the season will come to this town
When I can get close to you

This moment
When the two of us cuddle up
To gaze at the first snow flower of the year
Is overflowing with happiness

It's not dependence or weakness
I just love you
I thought so with all my heart

I feel like when I'm with you
I can overcome anything
I pray that these days
Will continue forever

The wind rattled the window
The night shakes you awake
I will change any sorrow
Into a smile

The snow flowers fell
Outside the window
Unceasing
And colored our town
I realized that love means
Wanting to do something
For someone else

If I should lose you
I'll become a star and shine on you
I'll be with you even on nights
When your smile is wet with tears

This moment
When the two of us cuddle up
To gaze at the first snow flower of the year
Is overflowing with happiness

It's not dependence or weakness
I just want to be like this
With you forever
I can honestly think that now

The pure white snow flowers
Bury this town
Softly drawing memories in our hearts
Together forever with you...

*/

#include <bits/stdc++.h>

using namespace std;

const int N = 2e5 + 5;

int cnt[N];

struct segtree {
  segtree(int n) : n(n) {
    num.resize(n << 2);
    c.resize(n << 2);
    build(1, 0, n - 1);
  }
  void build(int p, int l, int r) {
    c[p] = 0;
    if (l == r) {
      num[p] = cnt[l];
      return;
    }
    int mid = (l + r) >> 1;
    build(p + p, l, mid);
    build(p + p + 1, mid + 1, r);
    num[p] = num[p + p] + num[p + p + 1];
  }
  void relax(int p, int l, int r) {
    if (c[p]) {
      num[p] = r - l + 1 - num[p];
      if (l < r) {
        c[p + p] ^= 1;
        c[p + p + 1] ^= 1;
      }
      c[p] = 0;
    }
  }
  void combine(int p, int l, int r) {
    num[p] = num[p + p] + num[p + p + 1];
  }
  void change(int l, int r) {
    change(1, 0, n - 1, l, r);
  }
  void change(int p, int l, int r, int ll, int rr) {
    relax(p, l, r);
    if (ll <= l && r <= rr) {
      c[p] ^= 1;
      relax(p, l, r);
      return;
    }
    if (r < ll || rr < l) return;
    int mid = (l + r) >> 1;
    change(p + p, l, mid, ll, rr);
    change(p + p + 1, mid + 1, r, ll, rr);
    combine(p, l, r);
  }
  int find(int l, int r) {
    return find(1, 0, n - 1, l, r);
  }
  int find(int p, int l, int r, int ll, int rr) {
    relax(p, l, r);
    if (ll <= l && r <= rr) return num[p];
    if (r < ll || rr < l) return 0;
    int mid = (l + r) >> 1;
    int ret = find(p + p, l, mid, ll, rr) + find(p + p + 1, mid + 1, r, ll, rr);
    combine(p, l, r);
    return ret;
  }
  int n;
  vector<int> num, c;
};


vector<int> edge[N];
int p[N], l[N], r[N], pt, a[N];

void dfs(int now) {
  l[now] = r[now] = pt;
  cnt[pt] = a[now];
  pt++;
  for (auto it : edge[now]) {
    dfs(it);
    r[now] = pt - 1;
  }
}

char buf[10];

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 2; i <= n; i++) {
    scanf("%d", p + i);
    edge[p[i]].push_back(i);
  }
  for (int i = 1; i <= n; i++) scanf("%d", a + i);
  dfs(1);
  //for (int i = 1; i <= n; i++) printf("%d %d %d\n", i, l[i], r[i]);
  
  segtree seg(n);

  int q;
  scanf("%d", &q);
  while (q--) {
    int v;
    scanf("%s %d", buf, &v);
    if (buf[0] == 'g') {
      printf("%d\n", seg.find(l[v], r[v]));
    } else {
      seg.change(l[v], r[v]);
    }
  }

  return 0;
}
