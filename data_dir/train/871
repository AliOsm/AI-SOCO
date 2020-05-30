#include<bits/stdc++.h>
using namespace std;

int a[1000006];
int main(){
    int n,m,k; cin>>n>>m>>k;
    for(int i=0;i<n;++i){
        int t; cin>>t; ++a[t];
    }
    int now=0,ans=0;
    for(int i=1;i<m;++i){
        now+=a[i];
        while(now>=k)--now,--a[i],++ans;
    }
    for(int L=0,R=m;R<=1000000;++L,++R){
        now-=a[L];
        now+=a[R];
        while(now>=k)--now,--a[R],++ans;
    }
    cout<<ans<<endl;
}
