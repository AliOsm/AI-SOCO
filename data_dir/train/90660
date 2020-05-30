#include<bits/stdc++.h>
using namespace std;

vector<pair<int,int>> G[100005];
vector<int> z;

bitset<100005> v;
int val[100005];

void upd(int val){
    for(int i:z)val=min(val,val^i);
    if(val)z.push_back(val);
}

void dfs(int now,int nval){
    val[now]=nval;
    v[now]=1;
    for(auto i:G[now]){
        if(v[i.first])upd(nval^val[i.first]^i.second);
        else dfs(i.first,nval^i.second);
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n,m; cin>>n>>m;
    while(m--){
        int u,v,w; cin>>u>>v>>w;
        G[u].push_back({v,w});
        G[v].push_back({u,w});
    }
    dfs(1,0);
    int mx=val[n];
    for(int i:z)mx=min(mx^i,mx);
    cout<<mx<<endl;
}
