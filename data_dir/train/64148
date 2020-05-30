#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define DEBUG
#ifdef DEBUG
#define debug(...) __f(#__VA_ARGS__, __VA_ARGS__)
	template <typename Arg1>
	void __f(const char* name, Arg1&& arg1){
		cerr << name << " : " << arg1 << std::endl;
	}
	template <typename Arg1, typename... Args>
	void __f(const char* names, Arg1&& arg1, Args&&... args){
		const char* comma = strchr(names + 1, ','); cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
	}
#else
#define debug(...)
#endif
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	ll(a.size())
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<ll,ll>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;

typedef tree<int,null_type,less<int>,rb_tree_tag,tree_order_statistics_node_update> pbds;
// ordered_set X
//K-th smallest
//*X.find_by_order(k-1)
//NO OF ELEMENTS < A
//X.order_of_key(A)

const int L=1e6+7;
std::vector<char> v[L];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, l, k, cur = 0;
	cin >> n >> l >> k;
	string s;
	cin >> s;
	sort(all(s));
	int prvidx = 0, f = 0;
	char ch;
	FOR(i,0,l)
	{
		ch = s[cur + k - prvidx-1];
		// debug(i,prvidx,ch);
		f = 0;
		FOR(j,prvidx,k)
		{
			// debug(j,f,ch,s[cur]);
			if(f == 0 && ch == s[cur])
			{
				f = 1;
				prvidx = max(prvidx, j);
			}
			v[j].pb(s[cur++]);
		}
	}
	int tot;
	FOR(i,0,n)
	{
		tot = l - sz(v[i]);
		FOR(j,0,tot)
		{
			// debug(i,l,sz(v[i]));
			v[i].pb(s[cur++]);
		}
	}
	std::vector<string> str;
	FOR(i,0,n)
	{
		string c="";
		FOR(j,0,l)c += v[i][j];
		str.pb(c);
	}
	if(k > 1)sort(str.begin(), str.begin() + k - 1);
	if(k < n)sort(str.begin() + k + 1, str.end());
	trace(str,x)cout<<x<<ln;
	return 0;
}