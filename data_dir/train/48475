#include<bits/stdc++.h>
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
const int L=1e6+7;
map<ll,ll> counter;
ll fastexpo(ll x,ll y,ll m)
{
	ll temp=1;
	while(y>0)
	{
		if(y&1)temp = ((temp%m)*(x%m))%m;
		x = ((x%m)*(x%m))%m;
		y>>=1;
	}return temp;
}
int co[26];
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int t;
	 	cin >> t;
	 	string s;
	 	while(t--)
	 	{
	 		cin >> s;
	 		int len = s.length(), f=0;
	 		FOR(i,0,len/2)
	 		{
	 			if(s[i] != s[len-i-1])
	 			{
	 				f=1;
	 				break;
	 			}
	 		}
	 		if(f)
	 		{
	 			cout<<s<<ln;
	 			continue;
	 		}
	 		FOR(i,0,len)
	 		{
	 			co[s[i]-'a']++;
	 		}
	 		int cc=0;
	 		FOR(i,0,26)
	 		{
	 			if(co[i] > 0)cc++;
	 		}
	 		if(cc==1)
	 		{
	 			cout<<"-1\n";
	 			FOR(i,0,26)co[i]=0;
	 			continue;
	 		}
	 		FOR(i,0,len)
	 		{
	 			if(s[i] != s[0])
	 			{
	 				swap(s[i], s[0]);break;

	 			}
	 		}
	 		FOR(i,0,26)co[i]=0;
	 		cout<<s<<ln;

	 	}
		return 0;
}