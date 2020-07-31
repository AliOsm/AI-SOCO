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
typedef long long ll;
typedef long double ld;
map<string,ll> counter;
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
	 	int n,co=0;
	 	cin>>n;
	 	string s;
	 	FOR(i,0,n)
	 	{
	 		cin>>s;
	 		if(s=="red")
	 		{
	 			counter["Reality"]++;
	 		}
	 		if(s=="purple")
	 			counter["Power"]++;
	 		if(s=="green")counter["Time"]++;
	 		if(s=="blue")counter["Space"]++;
	 		if(s=="orange")counter["Soul"]++;
	 		if(s=="yellow")counter["Mind"]++;


	 	}
	 	if(counter["Reality"])co++;
	 	if(counter["Power"])co++;
	 	if(counter["Time"])co++;
	 	if(counter["Space"])co++;
	 	if(counter["Soul"])co++;
	 	if(counter["Mind"])co++;
	 	cout<<6-co<<ln;
	 	if(counter["Power"]==0)
	 		cout<<"Power"<<ln;
	 	if(counter["Time"]==0)
	 		cout<<"Time"<<ln;
	 	if(counter["Space"]==0)
	 		cout<<"Space"<<ln;
	 	if(counter["Soul"]==0)
	 		cout<<"Soul"<<ln;
	 	if(counter["Reality"]==0)
	 		cout<<"Reality"<<ln;
	 	if(counter["Mind"]==0)
	 		cout<<"Mind"<<ln;
		return 0;
}