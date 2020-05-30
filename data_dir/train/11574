#include<bits/stdc++.h>
#define lp(i,j,n) for(int i=j;i<n;i++)
using namespace std;

typedef long long ll;

ll a,b,p,n;
const int n_=1000005;
ll apow[n_];
ll power(ll a,ll b,ll mod){
    ll res=1;
    a%=mod;
    while(b){
        if(b&1ll)res=res*a%mod;
        a=a*a%mod;
        b>>=1ll;
    }
    return res;
}
ll inv(ll b){
    return power(b,p-2,p);
}
ll solve(ll start){
    if(start>n)return 0;
    return 1ll+(n-start)/(p*(p-1));
}
int main() {
    ios_base::sync_with_stdio(0);cin.tie(NULL);
    cin>>a>>b>>p>>n;
    ll binv=inv(b);
    lp(i,1,p)apow[i]=power(a,i,p);
    ll res=0;
    lp(i,1,min(n+1,p)){
        ll wanted=inv(apow[i])*b%p;
        ll steps=1ll*((((i-wanted)%p)+p)%p)*(p-1);
        res+=solve(i+steps);
    }
    cout<<res<<"\n";
}