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
#define MAXN 200005
#define MOD 998244353LL

void solve() {
	int n;
	cin >> n;
	if (n < 500) {
		int ans = 0;
		for (int a = 1; a < n; a++) {
			int b = n-a;
			if (a>b) ans++;
		}
		cout << ans << '\n';
	}
	else {
		int ans = n/2-5;
		for (int b = n/2-5+1; b < n; b++) {
			int a= n-b;
			if (a>b) ans++;
			else break;
		}
		cout << ans << '\n';
	}
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int t = 1;
	cin >> t;
	for (int no = 1; no <= t; no++) {
//		cout << "Case #" << no << ": ";
		solve();
	}

}