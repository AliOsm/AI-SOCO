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
const int L=1e5+7;
map<int,int> lef;
map<int,int> ri;
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
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int n, num;
	 	cin >> n;
	 	char ch;
	 	std::vector<int> lefty;
	 	std::vector<int> righty;
	 	while(n--)
	 	{
	 		cin >> ch >> num;
	 		if(ch =='L')
	 		{
	 			lefty.pb(num);
	 			lef[num] = sz(lefty);
	 		}
	 		else if(ch == 'R')
	 		{
	 			righty.pb(num);
	 			ri[num] = sz(righty);
	 		}
	 		else 
	 		{
	 			if(lef.find(num)!=lef.end())
	 			{
	 				cout<<min(sz(lefty) - lef[num], lef[num]+sz(righty)-1)<<ln;
	 			}
	 			else
	 			{
	 				cout<<min(sz(righty) - ri[num], ri[num]+sz(lefty)-1)<<ln;
	 			}
	 		}
	 	}
		return 0;
}