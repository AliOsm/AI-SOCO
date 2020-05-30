#include <bits/stdc++.h>

using namespace std;
using namespace placeholders;

template <class T> void mini(T &l, T r) {l = min(l, r);}
template <class T> void maxi(T &l, T r) {l = max(l, r);}

template <class TH> void _dbg(const char *sdbg, TH h) {
  cerr << sdbg << "=" << h << "\n";
}
template <class TH, class ...TA> void _dbg(const char *sdbg, TH h, TA ...a) {
  while (*sdbg != ',') cerr << *sdbg++; cerr << "=" << h << ","; _dbg(sdbg + 1, a...);
}
template <class T> ostream &operator<<(ostream &os, vector <T> v) {
  os << "[";
  for (auto vv : v) os << vv << ",";
  return os << "]";
}
template <class L, class R> ostream &operator<<(ostream &os, pair <L, R> p) {
  return os << "(" << p.first << "," << p.second << ")";
}

#define eput(...) //_dbg(#__VA_ARGS__, __VA_ARGS__)

using llint = long long;

const int N = 2e5 + 10, SIG = 27, L = 20;

namespace SA {
int sa[N], rk[N], ht[N], s[N << 1], t[N << 1], p[N], cnt[N], cur[N];
#define pushS(x) sa[cur[s[x]]--] = x
#define pushL(x) sa[cur[s[x]]++] = x
#define inducedSort(v) fill_n(sa, n, -1); fill_n(cnt, m, 0); \
  for (int i = 0; i < n; ++i) cnt[s[i]]++; \
  for (int i = 1; i < m; ++i) cnt[i] += cnt[i - 1]; \
  for (int i = 0; i < m; ++i) cur[i] = cnt[i] - 1; \
  for (int i = n1 - 1; ~i; --i) pushS(v[i]); \
  for (int i = 1; i < m; ++i) cur[i] = cnt[i - 1]; \
  for (int i = 0; i < n; ++i) if (sa[i] > 0 && t[sa[i] - 1]) pushL(sa[i] - 1); \
  for (int i = 0; i < m; ++i) cur[i] = cnt[i] - 1; \
  for (int i = n - 1; ~i; --i) if (sa[i] > 0 && !t[sa[i] - 1]) pushS(sa[i] - 1)

void sais(int n, int m, int *s, int *t, int *p) {
  int n1 = t[n - 1] = 0, ch = rk[0] = -1, *s1 = s + n;
  for (int i = n - 1; ~i; --i) t[i] = s[i] == s[i + 1] ? t[i + 1] : s[i] > s[i + 1];
  for (int i = 1; i < n; ++i) rk[i] = t[i - 1] && !t[i] ? (p[n1] = i, n1++) : -1;
  inducedSort(p);
  for (int i = 0, x, y; i < n; ++i) if (~(x = rk[sa[i]])) {
    if (ch < 1 || p[x + 1] - p[x] != p[y + 1] - p[y]) ch++;
    else for (int j = p[x], k = p[y]; j <= p[x + 1]; ++j, ++k)
      if ((s[j] << 1 | t[j]) != (s[k] << 1 | t[k])) {ch++; break;}
    s1[y = x] = ch;
  }
  if (ch + 1 < n1) sais(n1, ch + 1, s1, t + n, p + n1);
  else for (int i = 0; i < n1; ++i) sa[s1[i]] = i;
  for (int i = 0; i < n1; ++i) s1[i] = p[sa[i]];
  inducedSort(s1);
}
template<typename T>
int mapCharToInt(int n, const T *str) {
  int m = *max_element(str, str + n);
  fill_n(rk, m + 1, 0);
  for (int i = 0; i < n; ++i) rk[str[i]] = 1;
  for (int i = 0; i < m; ++i) rk[i + 1] += rk[i];
  for (int i = 0; i < n; ++i) s[i] = rk[str[i]] - 1;
  return rk[m];
}
template<typename T>
void suffixArray(int n, const T *str) {
  int m = mapCharToInt(++n, str);
  sais(n, m, s, t, p);
  for (int i = 0; i < n; ++i) rk[sa[i]] = i;
  for (int i = 0, h = ht[0] = 0; i < n - 1; ++i) {
    int j = sa[rk[i] - 1];
    while (i + h < n && j + h < n && s[i + h] == s[j + h]) ++h;
    if (ht[rk[i]] = h) h--;
  }
}
}


int n, k;
char *head[N];
char s[N];
int a[N];
int len[N];
int bl[N], bl1[N];
llint ans[N];
int len1[N], lenn[N];

struct Rmq {
  int n;
  int mn[N][L];

  void init(int a[N], int _n) {
    n = _n;
    for (int i = 2; i <= n; ++i) {
      mn[i][0] = a[i];
    }
    for (int j = 1; j < L; ++j) {
      for (int i = 2; i <= n; ++i) {
        int t = i + (1 << (j - 1));
        if (t > n) t = n;
        mn[i][j] = min(mn[i][j - 1], mn[t][j - 1]);
      }
    }
  }

  int rmq(int a, int b) {
    int d = b - a + 1;
    int t = 31 - __builtin_clz(d);
    return min(mn[a][t], mn[b - (1 << t) + 1][t]);
  }

  int pre(int a, int k) {
    int l = 1, r = a;
    while (l + 1 < r) {
      int mid = (l + r) >> 1;
      if (rmq(mid, a) >= k) {
        r = mid;
      } else {
        l = mid;
      }
    }
    return r;
  }

  int nxt(int a, int k) {
    int l = a, r = n + 1;
    while (l + 1 < r) {
      int mid = (l + r) >> 1;
      if (rmq(a, mid) >= k) {
        l = mid;
      } else {
        r = mid;
      }
    }
    return l;
  }

} rmq;

int ll[N];

void go_ll(int nn) {
  int l = 1;
  map <int, int> mp;
  bool ok = 0;

  for (int r = 1; r <= nn; ++r) {
    if (bl[r] != 0)
      mp[bl[r]] = r;
    for (; l <= r; ++l) {
      if (mp.size() >= k) {
        ok = 1;
        if (bl[l] == 0) {
        } else if (mp[bl[l]] == l) {
          mp.erase(bl[l]);
        }
        eput(l, bl[l]);
        eput(mp.size());
      } else {
        break;
      }
    }
    if (ok)
      ll[r] = l - 1;
    else
      ll[r] = -1;
  }

}

bool check(int x, int i) {
  int l;
  if (i == 1) l = 1;
  else {
    l = rmq.pre(i, x);
    if (rmq.rmq(l, i) >= x) --l;
  }
  int r;
  if (i == rmq.n) r = rmq.n;
  else {
    int t = rmq.nxt(i + 1, x);
    eput("hi", i, t, rmq.rmq(i + 1, t));
    if (rmq.rmq(i + 1, t) >= x) {
      r = t;
    } else {
      r = i;
    }
  }

  eput("ed", x, i, l, r);
  return ll[r] >= l;
}

int binary_s(int i) {
  int l = 0, r = lenn[i] + 1;
  while (l + 1 < r) {
    int mid = (l + r) >> 1;
    eput(mid, i, check(mid, i));
    if (check(mid, i)) {
      l = mid;
    } else {
      r = mid;
    }
  }
  return l;
}

void run() {
  scanf("%d%d", &n, &k);
  char *p = s;
  for (int i = 1; i <= n; ++i) {
    scanf("%s", p);
    head[i] = p;
    len[i] = strlen(p);
    p += len[i] + 1;
  }

  int nn = 0;
  for (int i = 1; i <= n; ++i) {
    for (int j = 0; j < len[i]; ++j) {
      bl1[nn] = i;
      len1[nn] = len[i] - j;
      a[nn++] = head[i][j] - 'a';
    }
    a[nn++] = i + 26;
  }

  SA::suffixArray(nn, a);

  for (int i = 0; i <= nn; ++i) eput(SA::sa[i]);
  for (int i = 1; i <= nn; ++i) eput(SA::rk[i]);
  for (int i = 1; i <= nn; ++i) eput(SA::ht[i]);
  SA::ht[1] = 0;
  
  for (int i = 1; i <= nn; ++i) {
    bl[i] = bl1[SA::sa[i]];
    lenn[i] = len1[SA::sa[i]];
  }
  
  rmq.init(SA::ht, nn); 
  go_ll(nn);

  for (int i = 1; i <= nn; ++i) eput(i, ll[i]);

  for (int i = 1; i <= nn; ++i) {
    int t = bl[i];
    int l = binary_s(i);
    eput(t, i, l);
    ans[t] += l;
  }

  for (int i = 1; i <= n; ++i) {
    printf("%lld%c", ans[i], " \n"[i == n]);
  }

}

int main() {
  run();
  return 0;
}
