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
int hedge[L], deg[L], done[L];
std::vector<int> v[L];
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int n,k,a,b;
	 	cin >> n >> k;
	 	FOR(i,0,n-1)
	 	{
	 		cin >> a>> b;
	 		v[a].pb(b);
	 		v[b].pb(a);
	 		deg[a]++;
	 		deg[b]++;
	 	}
	 	queue<int>q;
	 	FOR(i,1,n+1)
	 	{
	 		if(deg[i] == 1)
	 		{
	 			q.push(i);
	 			// hedge[i]=;
	 		}
	 	}
	 	int tmp,steps=0;
	 	while(1)
	 	{
	 		set<int>SET;
	 		while(sz(q))
	 		{
	 			tmp = q.front();
	 			// debug(tmp);
	 			done[tmp]=1;
	 			q.pop();
	 			trace(v[tmp],x)
	 			{
	 				if(done[x])continue;
	 				deg[x]--;
	 				SET.insert(x);
	 				hedge[x]++;
	 			}
	 		}
	 		// debug(sz(SET),sz(q));
	 		// if(sz(SET)==2 && sz(q)==2)
	 		// {
	 			// cout<<"No";
	 			// return 0;
	 		// }
	 		// debug(sz(SET));
	 		if(sz(SET)==0)break;
	 		trace(SET,x)
	 		{
	 			// debug(x,hedge[x]);
	 			if(done[x])
	 			{
	 				cout<<"No";
	 				return 0;
	 			}
	 			if(deg[x]>1 || hedge[x]<3)
	 			{
	 				// debug(x,deg[x],hedge[x]);
	 				cout<<"No";
	 				return 0;
	 			}
	 		}
	 		steps++;
	 		trace(SET,x)q.push(x);
	 	}	
	 	if(steps == k)
	 	cout<<"Yes";
	 	else cout<<"No";
		return 0;
}