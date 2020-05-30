#include<bits/stdc++.h>
using namespace std;
#define ll long long

int n;
unordered_map<long long,bool> mp;

stack<pair<int,int>> st;
int deg[100005];
void dfs(int now,int m){
    // cout<<now<<" "<<m<<endl;
    if(m==0){
        while(st.size()){
            cout<<st.top().first<<" "<<st.top().second<<endl;
            st.pop();
        }
        exit(0);
    }
    if(deg[now]>=2){
        for(int i=(now+1>n?now+1-m:now+1);i!=now;i=(i+1>n?i+1-n:i+1)){
            if(deg[i]<2)dfs(i,m);
        }
    }
    else for(int i=(now+1>n?now+1-n:now+1);i!=now;i=(i+1>n?i+1-n:i+1)){
        auto it=mp.find(((ll)now<<20)|i);
        if(deg[i]<2 and (it==mp.end() or it->second==0)){
            st.emplace(now,i);
            deg[now]++; deg[i]++;
            mp[((ll)now<<20)|i]=1;
            mp[((ll)i<<20)|now]=1;
            dfs(i,m-1);
            mp.erase(((ll)now<<20)|i);
            mp.erase(((ll)i<<20)|now);
            deg[now]--; deg[i]--;
            st.pop();
        }
    }
}

int main(){
    int m; cin>>n>>m;
    if(n<=500 and m*2>n*(n-1)/2)return cout<<-1<<endl,0;
    for(int i=0;i<m;++i){
        int u,v; cin>>u>>v;
        mp[(((ll)u)<<20)|v]=1;
        mp[(((ll)v)<<20)|u]=1;
    }
    for(int i=1;i<=n;++i){
        dfs(i,m);
    }
    cout<<-1<<endl;
}
