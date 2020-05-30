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
constexpr int N = 1e6 + 10, ALP = 26, INF = 0x3f3f3f3f; 
int n, q, a[N], triePos[N]; char s[N]; 

struct Trie {
	//0 type
	//1 connect
	struct node {
		int nx[ALP];
		int cnt, f[2];
		void init() { memset(nx, 0, sizeof nx); cnt = 0; f[0] = f[1] = INF; }
	}t[N];
	int tot, root;
	int newnode() { ++tot; t[tot].init(); return tot; } 
	void init() { tot = 0; root = newnode(); }
	int insert(int rt, int ch) {
		if (t[rt].nx[ch] == 0) t[rt].nx[ch] = newnode();
		rt = t[rt].nx[ch];
		return rt;
	}
	int dfs(int u) {
		int sum = t[u].cnt;
		for (int i = 0; i < 26; ++i) {
			int v = t[u].nx[i];
			if (!v) continue;
			if (t[u].cnt) chmin(t[v].f[0], min(t[u].f[0], t[u].f[1]) + 1);
			else chmin(t[v].f[0], t[u].f[0] + 1);
		    t[v].f[1] = t[u].f[0] + sum + 1;
			if (sum == 0) chmin(t[v].f[1], t[u].f[1]);
			else {
				if (t[v].cnt == 0) chmin(t[v].f[1], t[u].f[1] + sum);
				else chmin(t[v].f[1], t[u].f[1] + sum);
			}
			sum += dfs(v);
		}
		return sum; 
	}
}trie;

void run() {
	trie.init();
	triePos[0] = trie.root;
	for (int i = 1; i <= n; ++i) {
		int p; char t[10];
		cin >> p >> t;
		triePos[i] = trie.insert(triePos[p], *t - 'a');
	}
	rd(q);
	for (int i = 1; i <= q; ++i) {
		rd(a[i]);
		trie.t[triePos[a[i]]].cnt = 1;
	}
	trie.t[trie.root].f[0] = 0;
	trie.t[trie.root].f[1] = 1;
//	trie.t[trie.root].cnt = 1;
	trie.dfs(trie.root);
//	dbg(trie.t[triePos[1]].f[0], trie.t[triePos[1]].f[1]);
//	dbg(trie.t[triePos[5]].f[0], trie.t[triePos[5]].f[1]);
	for (int i = 1, p; i <= q; ++i) {
		p = a[i];
		cout << min(trie.t[triePos[p]].f[0], trie.t[triePos[p]].f[1]) << " \n"[i == q];
	}
}

int main() {
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
