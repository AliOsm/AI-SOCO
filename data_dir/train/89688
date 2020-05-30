#include<bits/stdc++.h>
using namespace std;

int ng[1111];
int main(){
    int n,m; cin>>n>>m;
    while(m--){
        int u,v; cin>>u>>v;
        ng[u]=ng[v]=1;
    }
    int mid=1;
    for(;;++mid){if(!ng[mid])break;}
    cout<<n-1<<endl;
    for(int i=1;i<=n;++i){
        if(i!=mid)cout<<i<<" "<<mid<<endl;
    }
}
