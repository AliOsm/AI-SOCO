#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define SZ(x) int((x).size())
#define endl "\n" 
using db = double;
using ll = long long;
using ull = unsigned long long; 
using pII = pair <int, int>;
using pLL = pair <ll, ll>;
constexpr int mod = 1e9 + 7;
template <class T1, class T2> inline void chadd(T1 &x, T2 y, int Mod = mod) { x += y; while (x >= Mod) x -= Mod; while (x < 0) x += Mod; } 
template <class T1, class T2> inline void chmax(T1 &x, T2 y) { if (x < y) x = y; }
template <class T1, class T2> inline void chmin(T1 &x, T2 y) { if (x > y) x = y; }
inline int nextInt() { int x; cin >> x; return x; }
void rd() {}
template <class T, class... Ts> void rd(T& arg, Ts&... args) { cin >> arg; rd(args...); }
#define dbg(x...) do { cout << "\033[32;1m" << #x << " -> "; err(x); } while (0) 
void err() { cout << "\033[39;0m" << endl; } 
template <class T, class... Ts> void err(const T& arg, const Ts&... args) { cout << arg << ' '; err(args...); }
template <template<typename...> class T, typename t, typename... A> 
void err(const T <t> &arg, const A&... args) { for (auto &v : arg) cout << v << ' '; err(args...); }
void ptt() { cout << endl; }
template <class T, class... Ts> void ptt(const T& arg, const Ts&... args) { cout << ' ' << arg; ptt(args...); }
template <class T, class... Ts> void pt(const T& arg, const Ts&... args) { cout << arg; ptt(args...); }
void pt() {}
template <template<typename...> class T, typename t, typename... A>
void pt(const T <t> &arg, const A&... args) { for (int i = 0, sze = arg.size(); i < sze; ++i) cout << arg[i] << " \n"[i == sze - 1]; pt(args...); }
inline ll qpow(ll base, ll n) { assert(n >= 0); ll res = 1; while (n) { if (n & 1) res = res * base % mod; base = base * base % mod; n >>= 1; } return res; }
//head
constexpr int N = 1e5 + 10;
const ll INF = 1e18;
int nr, ng, nb; 

struct Line {
	mutable ll k, m, p;
	bool operator < (const Line& o) const { return k < o.k; }
	bool operator < (ll x) const { return p < x; }
};

struct LineContainer : multiset<Line, less<>> {
	ll div(ll a, ll b) { return a / b - ((a ^ b) < 0 && a % b); }
	bool isect(iterator x, iterator y) {
		if (y == end()) { x->p = INF; return false; }
		if (x->k == y->k) x->p = x->m > y->m ? INF : -INF;
		else x->p = div(y->m - x->m, x->k - y->k);
		return x->p >= y->p;
	}
	void add(ll k, ll m) {
		auto z = insert({k, m, 0}), y = z++, x = y;
		while (isect(y, z)) z = erase(z);
		if (x != begin() && isect(--x, y)) isect(x, y = erase(y));
		while ((y = x) != begin() && (--x)->p >= y->p)
			isect(x, erase(y));
	}
	ll query(ll x) {
		if (empty()) return 0;
		auto it = lower_bound(x);
		assert(it != end());
		return (*it).k * x + (*it).m;
	}
};

ll gao(vector <ll> &A, vector <ll> &B, vector <ll> &C) {
	LineContainer lc;
	for (auto &it : C) {
		lc.add(-it, -it * it);
	}
	ll res = 9e18;
	for (auto &x : A) {
		int pos = lower_bound(B.begin(), B.end(), x) - B.begin();
		int l = max(0, pos - 20);
		int r = min(pos + 20, SZ(B) - 1);
		for (int i = l; i <= r; ++i) {
			ll y = B[i];
			ll now = x * x + y * y - x * y;
			ll tmp = -lc.query(-(x + y));
			now += tmp;
			chmin(res, now);
		}	
	}
	return res;
	
}

void run() {
	rd(nr, ng, nb);
	vector <ll> vecR(nr), vecG(ng), vecB(nb);
	for (auto &it : vecR) rd(it);
	for (auto &it : vecG) rd(it);
	for (auto &it : vecB) rd(it);
	sort(vecR.begin(), vecR.end());
	sort(vecG.begin(), vecG.end());
	sort(vecB.begin(), vecB.end());
	ll res = min({gao(vecR, vecG, vecB), gao(vecR, vecG, vecB), gao(vecG, vecR, vecB), gao(vecG, vecB, vecR), gao(vecB, vecR, vecG), gao(vecB, vecG, vecR)});
	pt(res * 2);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cout << fixed << setprecision(20);
	int _T = nextInt();
	while (_T--) run(); 
//    for (int kase = 1; kase <= _T; ++kase) {
//        cout << "Case #" << kase << ": ";
//        run();
//    }
//	while (cin >> n) run();
//	run();
	return 0;
}
