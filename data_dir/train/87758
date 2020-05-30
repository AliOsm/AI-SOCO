#include <cstdio>
#include <cstdlib>
#include <utility>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll, pii> plp;
const int maxn = 2e3 + 64;
const ll inf = 1e14;
int a[maxn];
int b[maxn];
plp c[maxn * (maxn - 1) / 2];
int k;
pii ans[2];
ll v;
int main()
{
	int n;
	ll sa = 0;
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", a + i);
		sa += a[i];
	}
	int m;
	ll sb = 0;
	scanf("%d", &m);
	for (int i = 0; i < m; ++i) {
		scanf("%d", b + i);
		sb += b[i];
	}
//k = 0
	v = abs(sa - sb);
//k = 1
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j) {
			ll d = abs(sa - sb - 2 * a[i] + 2 * b[j]);
			if (d < v) {
				k = 1;
				v = d;
				ans[0] = {i, j};
			}
		}
	int p = 0;
	if (n < 2 || m < 2)
		goto opt;
//k = 2
	// abs(sa - sb - 2(a[i1] + [ai2]) + 2(b[j1] + b[j2]))
	//=abs(2(b[j1] + b[j2]) - (-sa + sb + 2(a[i1] + [ai2])))
	for (int i = 0; i < n - 1; ++i)
		for (int j = i + 1; j < n; ++j)
			c[p++] = {-sa + sb + 2LL * (a[i] + a[j]), {i, j}};
	sort(c, c + p);
	for (int i = 0; i < m - 1; ++i)
		for (int j = i + 1; j < m; ++j) {
			ll u = 2LL * (b[i] + b[j]);
			int o = upper_bound(c, c + p, plp(u, {-1,-1})) - c;
			if (o < p) {
				ll d = c[o].first - u;
				if (d < v) {
					k = 2;
					v = d;
					ans[0] = {c[o].second.first, i};
					ans[1] = {c[o].second.second, j};
				}
			}
			if (--o >= 0) {
				ll d = u - c[o].first;
				if (d < v) {
					k = 2;
					v = d;
					ans[0] = {c[o].second.first, i};
					ans[1] = {c[o].second.second, j};
				}
			}
		}
opt:
	printf("%lld\n%d\n", v, k);
	for (int i = 0; i < k; ++i)
		printf("%d %d\n", ans[i].first + 1, ans[i].second + 1);
}
