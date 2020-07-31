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
string s, ns;
int counter[L];
int st[L];
void compress()
{
	ns = "";
	int n = s.length(), co = 1, cur = 0, idxprv = 0;
	char prv = s[0];
	FOR(i,1,n)
	{
		if(s[i] == prv)co++;
		else {
			counter[cur] = co;
			st[cur] = idxprv;
			co = 1;
			ns += prv;
			prv = s[i];
			idxprv = i;
			cur++;
		}
	}
	ns += prv;
	st[cur] = idxprv;
	counter[cur] = co;
	st[cur+1] = idxprv+1;
}
bool check(int x, int n)
{
	if(x >= 2)
	{
		if(s[x] == 'o' && s[x-1] == 'w' && s[x-2] == 't')return 1;
	}
	if(x <= n-3)
	{
		if(s[x] == 'o' && s[x+1] == 'n' && s[x+2] == 'e')return 1;
	}
	return 0;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t, tt;
	cin >> t;
	while(t--)
	{
		cin >> s;
		compress();
		int n = s.length(), ans = 0,c;
		std::vector<int> idx;
		FOR(i,0,n)
		{
			c = 0;
			if(s[i] == 'o')
			{
				int f =0, f1 = 0;
				if(i >= 2 && s[i-1] == 'w' && s[i-2] =='t')f = 1;
				if(i <= n-3 && s[i+1] == 'n' && s[i+2] =='e')f1 = 1;
				// debug(i,f,f1);
				if(f*f1)
				{
					idx.pb(i);
					s[i] = 'x';
				}
				else if(f)
				{
					if(i<n-1 && s[i+1] == 'o')
					{
						s[i-1] = 'x';
						idx.pb(i-1);
					}
					else 
					{
						s[i] = 'x';
						idx.pb(i);
					}
				}
				else if(f1)
				{
					if(i>0 && s[i-1] == 'o')
					{
						s[i+1] = 'x';
						idx.pb(i+1);
					}
					else 
					{
						s[i] = 'x';
						idx.pb(i);
					}
				}
			}
		}
		cout<<sz(idx)<<ln;
		trace(idx,x)
		{
			cout<<x+1<<" ";
		}
		cout<<ln;
	}
	return 0;
}