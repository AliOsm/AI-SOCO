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
constexpr int N = 1e5 + 10, M = 20; 
int n, a[N], pre[N], nx[N];
map <int, int> mp;

struct RMQ {
	int Max[N][M];
	int Min[N][M]; 
	int mm[N];
	void init(int n, int *b) {
		mm[0] = -1;
		for (int i = 1; i <= n; ++i) {
			mm[i] = ((i & (i - 1)) == 0) ? mm[i - 1] + 1 : mm[i - 1];
			Max[i][0] = b[i];
			Min[i][0] = b[i];
		}
		for (int j = 1; j <= mm[n]; ++j) {
			for (int i = 1; i + (1 << j) - 1 <= n; ++i) {
				Max[i][j] = max(Max[i][j - 1], Max[i + (1 << (j - 1))][j - 1]);
				Min[i][j] = min(Min[i][j - 1], Min[i + (1 << (j - 1))][j - 1]);
			}
		}
	}
	int queryMax(int x, int y) {
		int k = mm[y - x + 1];
		return max(Max[x][k], Max[y - (1 << k) + 1][k]);
	}
	int queryMin(int x, int y) {
		int k = mm[y - x + 1];
		return min(Min[x][k], Min[y - (1 << k) + 1][k]);  
	}
}rmq[2]; 

struct SEG {
	struct node {
		ll SL, SR, SPOS, LR, JL, tagL, tagR, cnt;
		node() { SL = SR = SPOS = LR = JL = cnt = 0; tagL = tagR = -1; }
		void upLR(ll _tagL, ll _tagR) {
			SL = _tagL * cnt % mod;
			SR = _tagR * cnt % mod;
			LR = _tagL * _tagR % mod * cnt % mod;
			JL = _tagL * SPOS % mod;
			tagL = _tagL;
			tagR = _tagR;
		}
		void upL(ll _tagL) {
			SL = _tagL * cnt % mod;
			LR = SR * _tagL % mod;
			JL = SPOS * _tagL % mod;
			tagL = _tagL;
		}
		void upR(ll _tagR) {
			SR = _tagR * cnt % mod;
			LR = SL * _tagR % mod;
			tagR = _tagR;
		}
		node operator + (const node &other) const {
			node res = node();
			res.SL = (SL + other.SL) % mod;
			res.SR = (SR + other.SR) % mod;
			res.SPOS = (SPOS + other.SPOS) % mod;
			res.LR = (LR + other.LR) % mod;
			res.JL = (JL + other.JL) % mod;
			res.cnt = (cnt + other.cnt) % mod; 
			return res;
		}
	}t[N << 2], res;
	void build(int id, int l, int r) {
		t[id] = node();
		if (l == r) {
			t[id].SPOS = l;
			t[id].cnt = 1;
			return;
		}
		int mid = (l + r) >> 1;
		build(id << 1, l, mid);
		build(id << 1 | 1, mid + 1, r);
		t[id] = t[id << 1] + t[id << 1 | 1];
	}
	void pushdown(int id) {
		ll &tagL = t[id].tagL;
		ll &tagR = t[id].tagR;
		if (tagL != -1 && tagR != -1) {
			t[id << 1].upLR(tagL, tagR);
			t[id << 1 | 1].upLR(tagL, tagR);
		} else if (tagL != -1) {
			t[id << 1].upL(tagL);
			t[id << 1 | 1].upL(tagL);
		} else if (tagR != -1) {
			t[id << 1].upR(tagR);
			t[id << 1 | 1].upR(tagR);
		}
		tagL = tagR = -1;
	}
	void update(int id, int l, int r, int ql, int qr, ll v, int opt) {
		if (ql > qr) return;
		if (l >= ql && r <= qr) {
			if (opt == 0) t[id].upL(v);
			else t[id].upR(v);
			return;
		}
		int mid = (l + r) >> 1;
		pushdown(id);
		if (ql <= mid) update(id << 1, l, mid, ql, qr, v, opt);
		if (qr > mid) update(id << 1 | 1, mid + 1, r, ql, qr, v, opt);
		t[id] = t[id << 1] + t[id << 1 | 1];
	}
	void query(int id, int l, int r, int ql, int qr) {
		if (ql > qr) return;
		if (l >= ql && r <= qr) {
			res = res + t[id];
			return;
		}
		int mid = (l + r) >> 1;
		pushdown(id);
		if (ql <= mid) query(id << 1, l, mid, ql, qr);
		if (qr > mid) query(id << 1 | 1, mid + 1, r, ql, qr);
	}
}seg;

void run() {
	for (int i = 1; i <= n; ++i) rd(a[i]);
	mp.clear();
	for (int i = 1; i <= n; ++i) {
		if (mp.count(a[i]) == 0) pre[i] = 1;
		else pre[i] = mp[a[i]] + 1;
		mp[a[i]] = i;
	}
	mp.clear();
	for (int i = n; i >= 1; --i) {
		if (mp.count(a[i]) == 0) nx[i] = n;
		else nx[i] = mp[a[i]] - 1;
		mp[a[i]] = i;
	}
	rmq[0].init(n, pre);
	rmq[1].init(n, nx);
	seg.build(1, 1, n);
	ll res = 0;
	for (int i = n - 1; i > 1; --i) {
		int l, r, mid, pos;
		int L = pre[i], R = nx[i];
		//L
		l = i + 1, r = n, pos = i;
		while (r - l >= 0) {
			mid = (l + r) >> 1;
			if (rmq[0].queryMax(i + 1, mid) < L) {
				pos = mid;
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		seg.update(1, 1, n, i, pos, L, 0);
		//R
		l = i + 1, r = n, pos = i;
		while (r - l >= 0) {
			mid = (l + r) >> 1;
			if (rmq[1].queryMin(i + 1, mid) > R) {
				pos = mid;
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		seg.update(1, 1, n, i, pos, R, 1);
		//query
		l = i + 1, r = n - 1, pos = i;
		while (r - l >= 0) {
			mid = (l + r) >> 1;
			if (rmq[0].queryMax(i, mid) <= i && rmq[1].queryMin(i, mid) >= mid) {
				pos = mid;
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		//dbg(i, pos);
		seg.res = SEG::node();
		seg.query(1, 1, n, i, pos);
		res += 1ll * i * seg.res.SR % mod + seg.res.JL - seg.res.LR - seg.res.SPOS * i % mod;
		res = (res % mod + mod) % mod;
	}
	pt(res);
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
