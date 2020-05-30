#include <bits/stdc++.h>
#define pii pair<int, int>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
using namespace std;

#define DEBUG 1
#define cerr if (DEBUG) cerr
#define test cerr << "hi\n";

#define INF 0x3f3f3f3f3f3f3f3f
#define MAXN 500005
#define MOD 998244353LL

long long a[MAXN], ps[MAXN];

void solve() {
	int n;
	long long x;
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	sort(a, a + n);
	reverse(a, a + n);
	partial_sum(a, a + n, ps+1);

	int ans = 0;
	for (int i = 1; i <= n; i++) {
		long long sum = ps[i];
		if (x*i <= sum) {
			ans = max(ans, i);
		}
	}

	cout << ans << '\n';

}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t = 1; cin >> t;
	while (t--) {
		solve();
	}
}