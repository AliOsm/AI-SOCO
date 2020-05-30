#include<bits/stdc++.h>
using namespace std;
map<int,vector<pair<int,int>>> mp;
int a[1505],pre[1505];
int main(){
    int n; cin>>n;
    for (int i=1;i<=n;++i)cin>>a[i];
    for(int i=1;i<=n;++i)pre[i]=pre[i-1]+a[i];
    for(int i=1;i<=n;++i){
        for(int j=i;j<=n;++j){
            mp[pre[j]-pre[i-1]].emplace_back(i,j);
        }
    }
    int mx=0,mxi=0;
    for(auto &p:mp){
        vector<pair<int,int>> &v=p.second;
        sort(v.begin(),v.end(),[&](const pair<int,int> &a,const pair<int,int> &b){ return a.second<b.second; });
        int R=0;
        int c=0;
        for(auto &p:v){
            if(p.first>R){
                R=p.second;
                ++c;
            }
        }
        if(c>=mx){
            mx=c;
            mxi=p.first;
        }
    }
    cout<<mx<<endl;
    auto v=mp[mxi];
    int R=0;
    for(auto &p:v){
        if(p.first>R){
            R=p.second;
            cout<<p.first<<" "<<p.second<<endl;
        }
    }
}
