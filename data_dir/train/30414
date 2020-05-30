/*
  All ghosts with the same V[y]-a*V[x] will collide except if they
  have the same V[x],V[y]

  The key idea was to use the fact that they were in the same line
  to eliminate Xs, Ys from the equation.
*/

#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define pb(x) push_back(x)
#define fi first
#define se second

typedef long long ll;

using namespace std;


int n;
ll a,b;
const int N=200001;

ll x[N],y[N];

map<pair<ll,ll> ,int>mp;
map<ll,int> cnt;
int main() {
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    #endif

	scanf("%d%lld%lld",&n,&a,&b);
	REP(i,n){
		int dum;
		scanf("%d",&dum);
		scanf("%lld%lld",&x[i],&y[i]);
		mp[{x[i],y[i]}]++;
	}
	ll r=0;
	for(auto i:mp){
		ll he=i.fi.se-a*i.fi.fi;
		r+=1ll*cnt[he]*i.se;
		cnt[he]+=i.se;
	}
	printf("%lld\n", r*2);
    return 0;
}