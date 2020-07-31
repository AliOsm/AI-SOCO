#pragma GCC optimize("Ofast,unroll-loops,no-stack-protector,fast-math")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include <bits/stdc++.h>
#define fi first
#define se second
#define endl "\n" 
using namespace std;
using db = double;
using ll = long long;
using ull = unsigned long long; 
using pII = pair <int, int>;
using pLL = pair <ll, ll>;
constexpr int mod = 1e9 + 7;
template <class T1, class T2> inline void chadd(T1 &x, T2 y) { x += y; while (x >= mod) x -= mod; while (x < 0) x += mod; } 
template <class T1, class T2> inline void chmax(T1 &x, T2 y) { if (x < y) x = y; }
template <class T1, class T2> inline void chmin(T1 &x, T2 y) { if (x > y) x = y; }
inline int rd() { int x; cin >> x; return x; }
template <class T> inline void rd(T &x) { cin >> x; }
template <class T> inline void rd(vector <T> &vec) { for (auto &it : vec) cin >> it; }  
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
ll gcd(ll a, ll b) { return b ? gcd(b, a % b) : a; }
inline ll qpow(ll base, ll n) { ll res = 1; while (n) { if (n & 1) res = res * base % mod; base = base * base % mod; n >>= 1; } return res; }
//head
ll n, k, bit[100];
inline int getLow(ll x, int bit) {
	return (x >> bit) % 2; 
}
inline void setOne(ll &x, int bit) {
	x |= (1ll << bit); 
}
inline void setZero(ll &x, int bit) {
	x |= (1ll << bit);
	x ^= (1ll << bit); 
}
ll gao() {
	ll res = 1, num = 0, suf = 0;
	for (int i = 1; i < 62; ++i) {
		if (bit[i] >= k) {
			suf = k - bit[i - 1] - 1;
			num = i;
			break;
		}
	}
	bool large = 0;
	for (int i = num - 1; i >= 0; --i) {
		int a = getLow(suf, i);
		int b = getLow(n, i);
		if (a == b) continue;
		if (a > b) large = 1;
		break;
	}
	res = n;
	if (large) {
		for (int i = num; i < 62; ++i) {
			if (getLow(res, i) == 1) {
				setZero(res, i);
				for (int j = i - 1; j >= num; --j)
					setOne(res, j);
				break;
			}
		}
	}
	res >>= num;
    return res;	
}
ll gao1() {
	ll res = 1, num = 0, suf = 0;
	for (int i = 1; i < 62; ++i) {
		if (bit[i] - 1 >= k) {
			suf = k - bit[i - 1];
			num = i;
			break;
		}
	}
	bool large = 0;
	for (int i = num - 1; i >= 0; --i) {
		int a = getLow(suf, i);
		int b = getLow(n, i);
		if (a == b) continue;
		if (a > b) large = 1;
		break;
	}
	res = n;
	if (large) {
		for (int i = num; i < 62; ++i) {
			if (getLow(res, i) == 1) {
				setZero(res, i);
				for (int j = i - 1; j >= num; --j)
					setOne(res, j);
				break;
			}
		}
	}
	res >>= num; 
	res <<= 1;
	return res;
}
void run() {
	if (k == 1) return pt(n);
	if (k == n) return pt(1);
	return pt(max(gao(), gao1()));
}

int main() {
	bit[0] = 1;
	for (int i = 1; i < 62; ++i) {
		bit[i] = bit[i - 1] << 1;
	}
	for (int i = 1; i < 62; ++i)
		bit[i] += bit[i - 1];
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cout << fixed << setprecision(20);
	while (cin >> n >> k) run();
	return 0;
}
