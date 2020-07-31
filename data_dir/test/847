#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define lb(x) ((x)&-(x))

const ll mod=1000000007;
ll bit[1000006],rep[1000006];

void add(int x,ll v){
    for(;x<1000006;x+=lb(x))bit[x]=(bit[x]+v)%mod;
}
ll query(int x,ll rt=0){
    for(;x;x-=lb(x))rt=(rt+bit[x])%mod;
    return rt;
}

int main(){
    int n; cin>>n;
    ll ans=0;
    while(n--){
        ll x; cin>>x;
        ll q=query(x);
        ++q;
        q-=rep[x];
        if(q<0)q=(q%mod+mod)%mod;
        rep[x]=(rep[x]+q)%mod;
        q*=x;
        q%=mod;
        ans+=q;
        add(x,q);
    }
    cout<<ans%mod<<endl;
}
