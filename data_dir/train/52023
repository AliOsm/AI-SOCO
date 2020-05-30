#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define pii pair<ll,ll>
#define sz(a)	ll(a.size())
#define debug1(x) cout<<x<<endl
#define debug2(x,y) cout<<x<<"-->"<<y<<endl
#define debug3(x,y,z) cout<<x<<"-->"<<y<<"-->"<<z<<endl
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;
map<ll,ll> counter;
int mark[200002];
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	string s;
	 	char prevch='A';
	 	cin>>s;
	 	int aux=0,len=s.length(),prev=0;
	 	if(len<=2){cout<<s;return 0;}
	 	// if(s[0]==s[1] && s[1]==s[2])mark[0]=1,prevch=s[0],prev=2;
		if(s[0]==s[1])prevch=s[0],prev=2;
		else prevch=s[1],prev=1;
		FOR(i,2,len)
		{
			if(s[i]==prevch)
			{
				prev++;
				if(prev>2)mark[i]=1,--prev;
				if(prev==2 && aux==2)mark[i]=1,--prev;
			}
			else prevch=s[i],aux=prev,prev=1;
		}
		FOR(i,0,len)if(!mark[i])cout<<s[i];
		return 0;
}