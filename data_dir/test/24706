#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double


int n,k,cf[200008];
ll pre[200008],t[200008];
ld revpre[200008],prepre[200008],dp[200008];

/* ld get(int l,int r){
    return -prepre[l-1]+revpre[l-1]*pre[l-1]+prepre[r]-revpre[r]*pre[l-1];
} */

struct line{
    ld a,b; int i;
    line(ld a,ld b,int i):a(a),b(b),i(i){}
    ld get(ld x){return a*x+b;}
};

// dp[i]=mindp[j-1]+cost+seg[j:i]
// def of "seg", see get(j,i)

bool jizz(line nw,line la,line lb){
    ld xx=(lb.b-la.b)/(la.a-lb.a);
    return nw.get(xx)<la.get(xx);
}

int use(ld cost){
    memset(dp,0,sizeof(dp));
    deque<line> dq; 
    // dq.push_back({-revpre[1],-prepre[1]+revpre[1]*pre[1],0});
    // dp[1]=1;
    dq.push_back({0,0,0});
    for(int i=1;i<=n;++i){
        while(dq.size()>1 && dq[0].get(revpre[i]) > dq[1].get(revpre[i]))dq.pop_front();
        dp[i]=dq[0].get(revpre[i])+prepre[i]+cost;
        cf[i]=dq[0].i;
        line nw(-pre[i],-prepre[i]+revpre[i]*pre[i]+dp[i],i);
        while(dq.size()>1 && jizz(nw,dq.back(),dq[dq.size()-2]))dq.pop_back();
        dq.push_back(nw);
    }
    int u=0,i=n;
    while(i){
        ++u;
        i=cf[i];
    }
    // cout<<"cost: "<<cost<<" , u: "<<u<<endl;
    // cout<<"dp: "; for(int i=1;i<=n;++i)cout<<dp[i]<<" "; cout<<endl;
    return u;
}

int main(){
    // srand(time(0));
    // n=200000,k=1;
    // for(int i=1;i<=n;++i)t[i]=(abs(rand()*rand())%100000+1,(n-i<300?1:100000));
    cin>>n>>k;
    for(int i=1;i<=n;++i)cin>>t[i];
    // pre[i]=pre[i-1]+t[i],rev[i]=rev[i-1]+((ld)1)/t[i];
    for(int i=1;i<=n;++i){
        pre[i]=pre[i-1]+t[i];
        prepre[i]=prepre[i-1]+(ld)pre[i]/t[i];
        revpre[i]=revpre[i-1]+((ld)1)/t[i];
    }

    ld L=0,R=1e20*n/k,ans=1e40;
    int timer=87;
    while(timer--){
        ld M=(L+R)/2;
        if(use(M)>k)L=M;
        else R=M,ans=min(ans,dp[n]);
    }
    // cout<<"cost: "<<L<<endl;
    cout<<fixed<<setprecision(20)<<ans-L*k<<endl;
}
