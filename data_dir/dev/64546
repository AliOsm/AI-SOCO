#include <bits/stdc++.h>
#define pii pair<long long, long long>
#define fi first
#define se second
#define pb push_back
#define mp make_pair
using namespace std;

#define DEBUG 1
#define cerr if (DEBUG) cerr
#define test cerr << "hi\n";
#define INF 0x3f3f3f3f3f3f3f3f

#define MAXN 500005
#define MOD 998244353LL

int n;
long long a[MAXN], ps[MAXN];

void solve() {
	cin >> n;
	long long ans = 0;
	for (int i = 0; i < n; i++) cin >> a[i];
	partial_sum(a, a+n, ps+1);

	set<long long> s;
	for (int l = 0, r = 0; l <= n; l++) {
		while (r <= n && !s.count(ps[r])) {
			s.insert(ps[r]);
			r++;
		}
		ans += r-l-1;
		s.erase(ps[l]);
	}
	cout << ans << '\n';

}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t = 1;
	while (t--) {
		solve();
	}
}