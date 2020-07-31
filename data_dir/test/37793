#include <bits/stdc++.h>
using namespace std;
#define fi first
#define se second
#define SZ(x) ((int)(x).size())
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
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
int n; 

vector <vector<int>> vec(10);

void run() {
	rd(n);
	if (n <= 3) return pt(-1);
	if (n <= 8) pt(vec[n]);
	else {
		int M = n % 4 + 4;
		n -= M;
		vector <int> res;
		for (int i = 0; i < n; i += 4) {
			res.push_back(i + 2);
			res.push_back(i + 4);
			res.push_back(i + 1);
			res.push_back(i + 3);
		}
		for (auto &it : vec[M]) {
			res.push_back(n + it);
		}
		pt(res);
	}	

}

bool ok(vector <int> &vec) {
	for (int i = 1; i < SZ(vec); ++i) {
		int gap = abs(vec[i] - vec[i - 1]);
		if (gap < 2 || gap > 4) return false;
	}
	return true;
}

vector<int> gao(int n) {
	vector <int> vec;
	for (int i = 1; i <= n; ++i) vec.push_back(i);
	vector <int> res;
	do {
		if (ok(vec)) {
			if (res.empty())
				res = vec;
			else if (vec < res) {
				res = vec;
			}
		}
	} while (next_permutation(all(vec)));
	return res;
	//pt(n);
	//pt(res);
}

int main() {
	for (int i = 4; i <= 8; ++i)
		vec[i] = gao(i);
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
