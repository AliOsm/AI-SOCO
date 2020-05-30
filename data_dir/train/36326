#include<bits/stdc++.h>
using namespace std;
#define ll long long

const ll mod=1000000007;

ll pw(ll b,ll n,ll m=mod,ll a=1){
    while(n){
        if(n&1)a=a*b%m;
        b=b*b%m; n>>=1;
    } return a;
}

ll fac[1000006],ifac[1000006],pr[1004];

ll C(ll n,ll m){
    return fac[n]*ifac[m]%mod*ifac[n-m]%mod;
}


int32_t main(){
    ll n,m,k; cin>>n>>m>>k;
    [&](){
        fac[0]=1;
        for(int i=1;i<1000006;++i)fac[i]=fac[i-1]*i%mod;
        ifac[1000005]=pw(fac[1000005],mod-2);
        for(int i=1000004;i>=0;--i)ifac[i]=ifac[i+1]*(i+1)%mod;
        pr[1]=1;
        for(int i=2;i<=n;++i){
            for(int j=0;j<=i;++j){
                pr[i]+=C(i,j)*pw(i-j,n)%mod*(j&1?-1:1);
            }
            pr[i]%=mod; pr[i]+=mod; pr[i]%=mod;
        }
    }();
    ll ans=0;
    if(m==1)ans=pw(k,n);
    else for(int i=1;i<=n;++i){
        for(int j=0;j<=i;++j){
            ll add=C(k,j)*C(k-j,i-j)%mod*C(k-j-(i-j),i-j)%mod;
            // cout<<i<<" "<<j<<" "<<add<<endl;
            add=add*pr[i]%mod*pr[i]%mod;
            // cout<<i<<" "<<j<<" "<<add<<endl;
            add=add*pw(j,n*(m-2))%mod;
            // cout<<i<<" "<<j<<" "<<add<<endl;
            ans+=add;
        }
    }
    ans%=mod; ans+=mod;
    cout<<ans%mod<<endl;
}
