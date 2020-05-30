#include<bits/stdc++.h>
using namespace std;

vector<int> G[3009];
int dist[3009];
void dfs(int now){
    for(int &ii:G[now])++dist[ii];
}
int main(){
    int n,m; cin>>n>>m;
    while(m--){
        int u,v; cin>>u>>v;
        G[u].push_back(v);
    }
    long long ans=0;
    for(int i=1;i<=n;++i){
        memset(dist,0,sizeof(dist));
        for(int &ii:G[i])dfs(ii);
        for(int j=1;j<=n;++j){
            if(i==j)continue;
            ans+=dist[j]*(dist[j]-1)/2;
        }
    }
    cout<<ans<<endl;
}
