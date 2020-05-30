#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,m,k; cin>>n>>m>>k;
    vector<int> mosq(k),step(m),ans;
    for(int i=0;i<m;++i)cin>>step[i];
    for(int i=0;i<k;++i)cin>>mosq[i];
    int mnj=995511;
    for(int i=0;i<m;++i){
        int cnt=0;
        for(int j=0;j<k;++j){
            if(mosq[j]<=n and mosq[j]%step[i]==0){
                ++cnt;
            }
        }
        if(cnt<mnj){
            mnj=cnt;
            ans.clear(); ans.push_back(i+1);
        }
        else if(cnt==mnj)ans.push_back(i+1);
    } cout<<ans.size()<<endl; for(int i:ans)cout<<i<<" ";
}
