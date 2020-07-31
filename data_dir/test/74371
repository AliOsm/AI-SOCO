#include <bits/stdc++.h>
#define fi first
#define se second
#define SZ(x) int((x).size())
#define endl "\n" 
using namespace std;
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
constexpr int N = 2e4 + 10; 
int n, m, K, f[60][N], g[60][N];
inline int getS(int id, int l, int r) { return g[id][r] - g[id][l - 1]; }
void run() {
	memset(f, 0, sizeof f);
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= m; ++j) {
			rd(g[i][j]);
			g[i][j] += g[i][j - 1];
		}
	}
	for (int i = 1; i + K - 1 <= m; ++i) {
		f[1][i] = getS(1, i, i + K - 1);
	}
	for (int i = 2; i <= n; ++i) {
		for (int j = 1; j + K - 1 <= m; ++j) {
			for (int k = j; k >= 1 && k + K - 1 >= j; --k) {
				chmax(f[i][j], f[i - 1][k] + getS(i, k, j + K - 1));
			}
			for (int k = j; k <= m && j + K - 1 >= k; ++k) {
				chmax(f[i][j], f[i - 1][k] + getS(i, j, k + K - 1));
			}
		}
		int Max = 0;
		for (int j = 1; j + K - 1 <= m; ++j) {
			if (j - K >= 1) chmax(Max, f[i - 1][j - K] + getS(i, j - K, j - 1));
			chmax(f[i][j], Max + getS(i, j, j + K - 1));
		}
		Max = 0;
		for (int j = m - K + 1; j >= 1; --j) {
			if (j + K <= m - K + 1) chmax(Max, f[i - 1][j + K] + getS(i, j + K, j + K + K - 1));
			chmax(f[i][j], Max + getS(i, j, j + K - 1));
		}
	}
	int res = 0;
	for (int i = 1; i <= m; ++i) chmax(res, f[n][i]);
	pt(res);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cout << fixed << setprecision(20);
	while (cin >> n >> m >> K) run(); 
//	while (cin >> n) run();
//    for (int kase = 1; kase <= _T; ++kase) {
//        cout << "Case #" << kase << ":\n";
//        run();
//    }
	return 0;
}
