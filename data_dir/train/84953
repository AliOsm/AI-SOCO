#include <bits/stdc++.h>
using namespace std;
#define D 19
typedef pair<int,int> pii;
typedef long long ll;
#define F first
#define S second
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a), end(a)
#define PB push_back
template<class T,class U>
ostream& operator << (ostream&out,const pair<T,U> & v)
{
	return out << '(' << v.F << ',' << v.S << ')';
}
template<class T>
ostream& operator << (ostream&out,const vector<T> & v)
{
	out << '[';
	for (int i = 0; i < SZ(v); ++i)
		out << v[i] << ",]"[i==SZ(v)-1];
	return out;
}
/**/
const int N = 1e5 + 987;
ll p[N],s;
vector<ll> v;
ll qry()
{
	int k = lower_bound(ALL(v),-s) - v.begin();
	ll ans = 1e18;
	if (k < SZ(v))
		ans = min(ans, abs(v[k] + s));
	if (--k >= 0)
		ans = min(ans, abs(v[k] + s));
	return ans;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, m, q;
	cin >> n >> m >> q;
	for (int i = 1; i <= n; ++i) {
		int k;
		cin >> k;
		s += ((i&1) ? 1 : -1) * k;
	}
	for (int i = 1; i <= m; ++i) {
		int k;
		cin >> k;
		p[i] = p[i-1] + ((i&1) ? -1 : 1) * k;
		if (i >= n)
			v.PB((((i-n)&1) ? -1 : 1) * (p[i] - p[i-n]));
	}
	sort(ALL(v));
	cout << qry() << '\n';
	while (q--) {
		int l,r,x;
		cin >> l >> r >> x;
		int w = r - l + 1;
		int odd;
		if (l&1) {
			odd = (w+1)/2;
		} else {
			odd = w/2;
		}
		s += x * 1LL * (odd * 2 - w);
		cout << qry() << '\n';
	}
}
