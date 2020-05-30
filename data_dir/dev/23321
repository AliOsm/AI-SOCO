#include<bits/stdc++.h>
using namespace std;

vector<int> G[500005],times;

void dfs(int now,int pa,int dep=1){
    if(G[now].size()==1u){
        times.push_back(dep);
    }
    for(int i:G[now]){
        if(i==pa)continue;
        dfs(i,now,dep+1);
    }
}

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    int n; cin>>n;
    for(int i=1,u,v;i<n;++i){
        cin>>u>>v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
    int mx=0;
    for(int i:G[1]){
        dfs(i,1);
        sort(times.begin(),times.end());
        for(int i=1;i<times.size();++i){
            times[i]=max(times[i],times[i-1]+1);
        }
        mx=max(mx,times.back());
        times.clear();
    }
    cout<<mx<<endl;
}
