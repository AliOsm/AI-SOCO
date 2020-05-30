#include <bits/stdc++.h>

using namespace std;

#define long long long
#define double __float128
#define INF (long) 1e18
#define MOD ((long) 1e9 + 7)
#define mll map<long, long>
#define pll pair<long, long>
#define umap unordered_map
#define umll umap<long, long>
#define pb push_back
#define FOR(i, a, b) \
  for (long i = a; i < (long) b; i++)
#define SORT(v, atr) \
  sort(v.begin(), v.end(), \
    [](auto &a, auto &b) { return a.atr < b.atr; });
#define UNSORT(v, atr) \
  sort(v.begin(), v.end(), \
    [](auto &a, auto &b) { return a.atr > b.atr; });
#define PRINTV(v) \
  FOR (_i, 0, v.size()) \
    cout << v[_i] << " "; \
  cout << "\n";

set<long> gera_primos(long n)
{
  set<long> primos;
  vector<bool> crivo(n+1);
  primos.insert(2);
  for (long i = 3; i <= n; i += 2) {
    if (crivo[i]) continue;
    primos.insert(i);
    for (long j = i; j <= n; j += i) {
      crivo[j] = true;
    }
  }
  return primos;
}

struct Link
{
  long from, to, cost;
};

struct Node
{
  bool visitado = false;
  bool cor = false;
  vector<long> in, out;
};

long a[10'000'010];

int main()
{
  ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);

  long n;
  cin >> n;

  auto primos = gera_primos(1e7);
  mll d;
  FOR (i, 0, n) {
    long x;
    cin >> x;
    a[x]++;
  }
  FOR (i, 1, 1e7) {
    for (auto &p : primos) {
      long k = i * p;
      if (k > 1e7) break;
      if (a[k] != 0) {
        d[p] += a[k];
      }
    }
  }
  auto it = primos.end();
  long ant = INF;
  do {
    it--;
    long p = *it;
    d[p] += d[ant];
    ant = p;
  } while (it != primos.begin());

  long m;
  cin >> m;
  while (m--) {
    long l, r;
    cin >> l >> r;

    auto it = d.lower_bound(l);
    long pl = it->first;
    auto jt = d.upper_bound(r);
    long pr = jt->first;

    long resp = d[pl] - d[pr];
    cout << resp << "\n";
  }
}
