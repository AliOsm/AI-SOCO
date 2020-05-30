#include<bits/stdc++.h>
using namespace std;

map<int,vector<pair<int,int>>> mp;

int F(int x,vector<int> &djs){
    return x==djs[x]?x:djs[x]=F(djs[x],djs);
}
void U(int x,int y,vector<int> &djs){
    djs[F(x,djs)]=F(y,djs);
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,m; cin>>n>>m;
    while(m--){
        int u,v,w; cin>>u>>v>>w;
        mp[w].emplace_back(u,v);
    }
    
    int L=1,R=1000000000;
    while(L<R){
        int M=(L+R)>>1;
        vector<int> djs(n+1);
        iota(djs.begin(),djs.end(),0);
        for(auto &p:mp){
            if(p.first>M)break;
            for(auto &pp:p.second)U(pp.first,pp.second,djs);
        }
        bool mer=1;
        for(int i=2;i<=n;++i)if(F(1,djs)!=F(i,djs))mer=0;
        if(mer)R=M;
        else L=M+1;
    }
    vector<int> djs(n+1);
    iota(djs.begin(),djs.end(),0);
    int cnt=0;
    int ans=0;
    for(auto &p:mp){
        if(p.first>L)break;
        cnt+=p.second.size();
        vector<pair<int,int>> con;
        for(auto &pp:p.second){
            if(F(pp.first,djs)==F(pp.second,djs))continue;
            else con.push_back(pp);
        }
        for(auto &pp:con){
            if(F(pp.first,djs)==F(pp.second,djs))++ans;
            else U(pp.first,pp.second,djs);
        }
    }
    /* int eff=0;
    for(auto &p:mp[L]){
        if(F(p.first,djs)!=F(p.second,djs))++eff;
        else ++ans;
    } */
    cout<<ans<<endl;
}
