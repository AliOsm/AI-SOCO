#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define pb push_back
#define eb emplace_back
#define ALL(x) (x).begin(), (x).end()
#define X first
#define Y second
// read integers
int RI() {return 0;}
template<typename T>
int RI(T & a)
{
	int c;
	int s = 1;
	while (!((c = getchar()) == '-' || isdigit(c) || c == EOF));
	if (c == EOF)
		return 0;
	if (c == '-') {
		s = -1;
		c = getchar();
	}
	a = 0;
	do {
		a = 10 * a + s * (c - '0');
	} while (isdigit(c = getchar()));
	return 1;
}
template<typename T, typename... Args>
int RI(T & a, Args & ... args) {return RI(a) ? 1 + RI(args...) : 0;}
//print integers, python style
template<typename T>
void __PI(T a)
{
	static const int maxd = 25;
	static char d[maxd];
	int i = maxd - 1;
	int s = a < 0 ? -1 : 1;
	do {
		d[--i] = s * (a % 10) + '0';
	} while (a /= 10);
	if (s < 0)
		d[--i] = '-';
	fputs(d + i, stdout);
}
template<char sep>
void __PSI() {}
template<char sep, typename T>
void __PSI(const T & a) {putchar(sep), __PI(a);}
template<char sep, typename T, typename... Args>
void __PSI(const T & a, const Args & ... args) {__PSI<sep, T>(a), __PSI<sep, Args...>(args...);}
template<char sep = ' ', char end = '\n', typename T, typename... Args>
void PI(const T & a, const Args & ... args) {__PI(a), __PSI<sep, Args...>(args...), putchar(end);}

const int maxn = 2.28e5;
int c[maxn];
int cnt[maxn]; // number of pink vertex in subtree
vector<int> g[maxn];
int dfs(int p, int u)
{
	if (c[u] < 0)
		cnt[u] = 1;
	for (auto v : g[u])
		if (v != p)
			cnt[u] += dfs(u, v);
	return cnt[u];
}
void tog(int u)
{
	printf(" %d", u);
	cnt[u] += c[u];
	c[u] *= -1;
}
void solve(int p, int u)
{
	if (!cnt[u])
		return;
	for (auto v : g[u])
		if (v != p) {
			if (cnt[v]) {
				cnt[u] -= cnt[v];
				tog(v);
				solve(u, v);
				tog(u);
			}
		}
	if (c[u] < 0) {
		if (u != 1) {
			tog(p);
			tog(u);
		} else {
			tog(g[1][0]);
			tog(1);
			tog(g[1][0]);
		}
	}
}
int main()
{
	int n;
	RI(n);
	rep(i,1,n+1)
		RI(c[i]);
	rep(i,1,n) {
		int x, y;
		RI(x, y);
		g[x].pb(y);
		g[y].pb(x);
	}
	dfs(0, 1);
	putchar('1');
	solve(0, 1);
	putchar('\n');
}
