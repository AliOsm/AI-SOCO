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
constexpr int N = 3e3 + 10; 
int n, fa[N], anc[N][N], sze[N], deep[N], dis[N][N], in[N], out[N]; ll f[N][N];
vector <vector<int>> G;
void pre(int u) {
	sze[u] = 1;
	in[u] = ++*in;
	for (auto &v : G[u]) if (v != fa[u]) {
		fa[v] = u;
		deep[v] = deep[u] + 1;
		pre(v);
		sze[u] += sze[v]; 
	}
	out[u] = *in;
}
void dfs(int rt, int u, int son) { 
	anc[rt][u] = son;
	for (auto &v : G[u]) if (v != fa[u]) {
		dfs(rt, v, son); 
	}
}
void run() {
	G.clear(); G.resize(n + 1);
	for (int i = 1, u, v; i < n; ++i) {
		cin >> u >> v;
		G[u].push_back(v);
		G[v].push_back(u);
	}
	memset(f, 0, sizeof f);
	for (int i = n; i >= 1; --i) {
		fa[i] = 0;
		deep[i] = 0;
		*in = 0;
		pre(i);
		for (int j = 1; j <= n; ++j) {
			dis[i][j] = dis[j][i] = deep[j];
		}
		for (auto &v : G[i]) {
			dfs(i, v, v); 
		}
	}
	vector <vector<pII>> vec(n + 1); 
	for (int i = 1; i <= n; ++i) {
		for (int j = i; j <= n; ++j) {
			vec[dis[i][j]].push_back(pII(i, j));  
		}
	}
	for (int i = 1; i <= n; ++i) {
		if (vec[i].empty()) break;
		for (auto &it : vec[i]) {
			if (in[it.fi] > in[it.se]) swap(it.fi, it.se);
			if (in[it.se] >= in[it.fi] && in[it.se] <= out[it.fi]) {
				chmax(f[it.fi][it.se], 1ll * (n - sze[anc[it.fi][it.se]]) * sze[it.se] + max(f[it.fi][fa[it.se]], f[it.se][anc[it.fi][it.se]]));
			} else {
				chmax(f[it.fi][it.se], 1ll * sze[it.fi] * sze[it.se] + max(f[fa[it.fi]][it.se], f[it.fi][fa[it.se]]));
			}
			chmax(f[it.se][it.fi], f[it.fi][it.se]);
		}
	}
	ll res = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j = i; j <= n; ++j) {
			chmax(res, f[i][j]);
		}
	}
	pt(res);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr); cout.tie(nullptr);
	cout << fixed << setprecision(20);
	while (cin >> n) run();
	return 0;
}
