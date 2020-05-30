#include <bits/stdc++.h>
using namespace std;

using pii = pair<int, int>; using vi = vector<int>;
template <class T> istream &operator>>(istream &, vector<T> &);
template <class T> ostream &operator<<(ostream &, const vector<T> &);
using ll = long long; using vll = vector<long long>;
constexpr int INF = 0x3f3f3f3f; constexpr ll BINF = 0x3f3f3f3f3f3f3f3fLL;

	const ll MOD = 1'000'000'007;

ll bigmod(ll b, ll p) {
	ll res = 1;
	for (;p;p>>=1,b=b*b%MOD) if (p & 1) res = res * b % MOD;
	return res;
}

ll getthing(ll x) {
	x--;
	if (x < 0) return 0;
	vector<ll> stripstarta, stripstartb;
	ll curidxa = 0, curidxb = 0;
	ll curidxg = 0;
	ll stripsize = 1;
	vector<ll> stripstartg;
	vector<ll> whichstrip, thatstripstart;
	for (int i=0;i<1000;i++) {
		if (i & 1) {
			thatstripstart.push_back(stripstartb.size());
			stripstartb.push_back(curidxb);
			curidxb += stripsize;
		} else {
			thatstripstart.push_back(stripstarta.size());
			stripstarta.push_back(curidxa);
			curidxa += stripsize;
		}
		whichstrip.push_back(i & 1);
		stripstartg.push_back(curidxg);
		curidxg += stripsize;
		stripsize *= 2;
		if (curidxg > 2e18) break;
	}
	ll mejm9 = 0;
	int wtf = 0;
	for (;;) {
		if (x >= stripstartg[wtf + 1]) {
			// this whole strip will be covered
			if (whichstrip[wtf]) {
				ll startidx = stripstartb[thatstripstart[wtf]];
				ll startnum = startidx * 2 + 2;
				ll striplen = stripstartb[thatstripstart[wtf] + 1] - startidx;
				ll endnum = startnum + (striplen - 1) * 2;
				// cerr << startnum << ' ' << endnum << ' ' << striplen << ' ' << wtf << ' ' << mejm9 << endl;
				mejm9 += ((startnum + endnum) % MOD) * (striplen % MOD) % MOD * bigmod(2, MOD - 2) % MOD;
			} else {
				ll startidx = stripstarta[thatstripstart[wtf]];
				ll startnum = startidx * 2 + 1;
				ll striplen = stripstarta[thatstripstart[wtf] + 1] - startidx;
				ll endnum = startnum + (striplen - 1) * 2;
				// cerr << startnum << ' ' << endnum << ' ' << striplen << ' ' << wtf << ' ' << mejm9 << endl;
				mejm9 += ((startnum + endnum) % MOD) * (striplen % MOD) % MOD * bigmod(2, MOD - 2) % MOD;
			}
			mejm9 %= MOD;
		} else {
			// calc this strip, break the thingy

			if (whichstrip[wtf]) {
				ll startidx = stripstartb[thatstripstart[wtf]];
				ll startnum = startidx * 2 + 2;
				ll striplen = x - stripstartg[wtf] + 1;
				ll endnum = startnum + (striplen - 1) * 2;
				// cerr << startnum << ' ' << endnum << ' ' << striplen << ' ' << wtf << ' ' << mejm9 << endl;
				mejm9 += ((startnum + endnum) % MOD) * (striplen % MOD) % MOD * bigmod(2, MOD - 2) % MOD;
			} else {
				ll startidx = stripstarta[thatstripstart[wtf]];
				ll startnum = startidx * 2 + 1;
				ll striplen = x - stripstartg[wtf] + 1;
				ll endnum = startnum + (striplen - 1) * 2;
				// cerr << startnum << ' ' << endnum << ' ' << striplen << ' ' << wtf << ' ' << mejm9 << endl;
				mejm9 += ((startnum + endnum) % MOD) * (striplen % MOD) % MOD * bigmod(2, MOD - 2) % MOD;
			}
			mejm9 %= MOD;
			break;
		}
		wtf++;
	}
	cerr << mejm9 << endl;
	return mejm9;
}

int solve() {
	ll l, r; cin >> l >> r;
	cout << (getthing(r) - getthing(l - 1) + MOD) % MOD << endl;
	return 0;
}

int main() {
	ios::sync_with_stdio(0);
	// precompute();
	// int t; cin >> t; for (int i=1;i<=t;i++)
	solve();
	// cout << (solve() ? "YES" : "NO") << endl;
	return 0;
}

template <class T> istream &operator>>(istream &is, vector<T> &v) {
	for (auto it=v.begin();it!=v.end();++it) is >> *it;
	return is;
}

template <class T> ostream &operator<<(ostream &os, const vector<T> &v) {
	for (auto it=v.begin();it!=v.end();) os << *it << " \n"[++it==v.end()];
	return os;
}
