#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a,b) 	for(int i=a;i<b;++i)
#define RFOR(i,a,b) 	for(int i=a;i>=b;--i)
#define ln 		"\n"
#define mp make_pair
#define pb push_back
#define sz(a)	ll(a.size())
#define debug1(x) cout<<x<<endl
#define debug2(x,y) cout<<x<<"-->"<<y<<endl
#define debug3(x,y,z) cout<<x<<"-->"<<y<<"-->"<<z<<endl
#define F first
#define S second
#define all(c)	c.begin(),c.end()
#define trace(c,x) for(auto &x:c)
#define pii pair<int,int>
typedef long long ll;
typedef long double ld;
typedef	priority_queue<pii,std::vector<pii>,greater<pii> > revpr;
const int L=1e5+7;
int a[L];
std::vector<int> out(L,-1);
std::map<int, int> counter;
struct node
{
	int curtime,val,q,type;
};
bool comp(node x, node y)
{
	return x.curtime<y.curtime;
}
int main()
{
		ios_base::sync_with_stdio(false);
	 	cin.tie(NULL);
	 	int n,val,type,curtime;
	 	cin>>n;
	 	std::vector<node> v(n);
	 	node temp;
	 	int prev=0,f=0;
	 	FOR(i,0,n)
		{
			cin>>type>>curtime>>val;
			v[i].curtime=curtime,v[i].val=val,v[i].q=i,v[i].type=type;
		}
		FOR(i,0,n)
		{
			if(v[i].type==3)
			{
				if(i==n-1)
				{
					sort(v.begin()+prev,v.begin()+n,comp);
						// cout<<prev<<" - "<<n-1<<ln;
					break;
				}
				FOR(j,i+1,n)
				{
					if(v[j].type==3)
					{
						if(j==n-1)
						{
							sort(v.begin()+prev,v.begin()+n,comp);
							// cout<<prev<<" - "<<j-1<<ln;
							i=n-1;
						}
						continue;
					}
					else
					{
						i=j-1;
						sort(v.begin()+prev,v.begin()+j-1,comp);
						// cout<<prev<<" - "<<j-1<<ln;
						prev=j;
						break;
					}
				}
			}
		}
		// cout<<ln;
		// trace(v,x)cout<<x.type<<" "<<x.curtime<<" "<<x.val<<ln;
		trace(v,x)
		{
			if(x.type==1)counter[x.val]++;
			else if(x.type==2)counter[x.val]--;
			else out[x.q]=counter[x.val];
		}
		FOR(i,0,n)
		{
			if(out[i]!=-1)cout<<out[i]<<ln;
		}
		return 0;
}