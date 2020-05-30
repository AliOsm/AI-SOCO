#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define all(v)  	((v).begin()),((v).end())
#define sz(x)  		((ll) (x).size())
#define clr(a,b)	memset(a,b,sizeof(a))
const double EPS = 1e-8;
const double pi = acos(-1);
ll dcmp(double a, double b) {
	return fabs(a - b) <= EPS ? 0 : a < b ? -1 : 1;
}
void debug() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
//	freopen("output.in", "wt", stdout);
#endif
}

ll const N = 1e5 + 9, M = 100 + 9, OO = 1e9;

ll fast_pow(ll x, ll y, ll mod) {
	ll res = 1;
	x = x % mod;
	while(y) {
		if(y&1)
			res = ((res% mod) * (x % mod)) % mod;
		y >>= 1;
		x = ((x % mod) * (x % mod)) % mod;
	}
	return res;
}

vector<vector<pair<ll, ll>>> vec(N);
bool vis[N];
ll cnt = 0;

void DFS(ll i) {
	++cnt;
	vis[i] = 1;
	for(auto it: vec[i]) {
		if(!vis[it.first] && !it.second)
			DFS(it.first);
	}
}

int main() {
	cout << fixed << setprecision(10);
	ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
	debug();
	ll n, k, mod = 1e9 + 7, u, v, w;
	cin >> n >> k;
	for (int i = 1; i < n; ++i) {
		cin >> u >> v >> w;
		--u, --v;
		vec[u].push_back({v, w});
		vec[v].push_back({u, w});
	}
	ll ans = fast_pow(n, k, mod);
	for (int i = 0; i < n; ++i) {
		if(vis[i])
			continue;
		cnt = 0;
		DFS(i);
		cnt = fast_pow(cnt, k, mod);
		ans -= cnt;
		if(ans < 0)
			ans += mod;
	}
	cout << ans;
	return 0;
}
