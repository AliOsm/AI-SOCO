#include<bits/stdc++.h>
using namespace std;

vector<pair<int,int>> edge;
vector<pair<int,int>> qs[10235];
int ans[20004],djs[555];

int F(int x){return x==djs[x]?x:djs[x]=F(djs[x]);}
bool u(int x,int y){
    x=F(x); y=F(y);
    if(x==y)return 0;
    djs[x]=y;
    return 1;
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,m; cin>>n>>m;
    edge.resize(m);
    for(int i=0;i<m;++i){
        cin>>edge[i].first>>edge[i].second;
    }
    int q; cin>>q; for(int i=0;i<q;++i){
        int l,r; cin>>l>>r; --l,--r;
        qs[l].push_back({r,i});
    }
    for(int i=0;i<m;++i){
        if(qs[i].empty())continue;
        sort(qs[i].begin(),qs[i].end());
        reverse(qs[i].begin(),qs[i].end());
        for(int i=1;i<=n;++i)djs[i]=i;
        int tot=n;
        for(int j=0;j<i;++j){
            if(u(edge[j].first,edge[j].second))--tot;
        }
        int ptr=m-1;
        for(auto q:qs[i]){
            while(ptr>q.first){
                if(u(edge[ptr].first,edge[ptr].second))--tot;
                --ptr;
            }
            ans[q.second]=tot;
        }
    }
    for(int i=0;i<q;++i)cout<<ans[i]<<'\n';
}
