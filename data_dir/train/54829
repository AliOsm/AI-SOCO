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
constexpr int N = 1e3 + 10, M = 4e5 + 10, ALP = 26;
constexpr ll INFLL = 0x3f3f3f3f3f3f3f3f;
int n, m; char s[M];
vector <int> subset[15];

struct ACAM {
	int nx[N][ALP];
	int fail[N], go[N];
	ll val[N], f[N][(1 << 14) + 5], g[N];
	int root, tot; 
	int que[N], ql, qr; 
	int newnode() { 
		++tot;
		memset(nx[tot], -1, sizeof nx[tot]);
		val[tot] = 0;
		return tot;
	}
	void init() { tot = 0; root = newnode(); }
	void insert(char *s, int _val) {
		int now = root;
		for (int i = 0; s[i]; ++i) {
			if (nx[now][s[i] - 'a'] == -1)
				nx[now][s[i] - 'a'] = newnode();
			now = nx[now][s[i] - 'a'];
		}
		val[now] += _val;
	}
	void build() {
		ql = 1, qr = 0;
		for (int i = 0; i < ALP; ++i) {
			if (nx[root][i] == -1) {
				nx[root][i] = root;
			} else {
				fail[nx[root][i]] = root;
				que[++qr] = nx[root][i];
			}
		}
		while (ql <= qr) {
			int now = que[ql++];
			for (int i = 0; i < ALP; ++i) {
				if (nx[now][i] == -1) {
					nx[now][i] = nx[fail[now]][i];
				} else {
					fail[nx[now][i]] = nx[fail[now]][i];
					val[nx[now][i]] += val[nx[fail[now]][i]];
					que[++qr] = nx[now][i];
				}
			}
		}
	}
	void gao() {
		build();
		rd(s);
		for (int i = 1; i <= tot; ++i) go[i] = i, g[i] = 0;
		memset(f, -0x3f, sizeof f);
		f[1][0] = 0;
		int cnt = 0, MaxBit = 14;
		for (int i = 0; s[i]; ++i) {
			if (s[i] == '?') {
				for (auto &mask : subset[cnt]) {
					for (int j = 1; j <= tot; ++j) {
						if (f[j][mask] > -INFLL) {
							for (int t = 0; t < MaxBit; ++t) {
								if (!((mask >> t) & 1)) {
									chmax(f[nx[go[j]][t]][mask | (1 << t)], f[j][mask] + g[j] + val[nx[go[j]][t]]);
								}
							}
						}		
					}
				}
				for (int j = 1; j <= tot; ++j) go[j] = j, g[j] = 0;
				++cnt;
			} else {
				for (int j = 1; j <= tot; ++j) {
					go[j] = nx[go[j]][s[i] - 'a'];
					g[j] += val[go[j]];
				}
			}
		}
		ll res = -INFLL;
		for (auto &mask : subset[cnt]) {
			for (int i = 1; i <= tot; ++i) {
				//dbg(i, f[i][mask], g[i]);
				chmax(res, f[i][mask] + g[i]);
			}
		}
		pt(res);
	}
}acam;

void run() {
	acam.init();
	for (int i = 1, c; i <= n; ++i) {
		rd(s, c);	
		acam.insert(s, c);
	}
	acam.gao();
}

int main() {
	for (int i = 0; i < 1 << 14; ++i) subset[__builtin_popcount(i)].push_back(i);
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cout << fixed << setprecision(20);
	while (cin >> n) run();
//    for (int kase = 1; kase <= _T; ++kase) {
//        cout << "Case #" << kase << ":\n";
//        run();
//    }
	return 0;
}
