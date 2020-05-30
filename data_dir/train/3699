#include <bits/stdc++.h>

using namespace std;

#define MOD 1000000007
#define ll long long int
#define ld long double
#define pb push_back
#define mkp make_pair
#define pii pair<int, int> 
#define pll pair<long long int, long long int>
#define sci(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define fi first
#define sc second
#define eps 1e-9

vector<pii> v[100];

int main()
{
	ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);

	ll n, m, h, i, j, k, x, y, z, a, b, c;
	ll ans = 0;
	cin >> n >> h >> m;
	for (i = 0; i < m; ++i) {
		cin >> x >> y >> z;
		v[x].pb(mkp(y, z));
	}
	multiset<pii> se;
	multiset<int> he;
	he.insert(h);
	for (i = 1; i <= n; ++i) {
		for (auto it: v[i]) {
			se.insert(it);
			he.insert(it.sc);
		}
		while (!se.empty()) {
			auto it = *se.begin();
			if (it.fi >= i) break;
			he.erase(he.find(it.sc));
			se.erase(se.begin());
		}
		ans += (*he.begin()) * (*he.begin());
	}
	cout << ans << endl;

	return 0;
}
