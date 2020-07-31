#include<bits/stdc++.h>
using namespace std;

int main(){
    int n; cin>>n;
    long long hi=5; while(hi<=n)hi*=10; hi/=10;
    if(hi==0)return cout<<n*(n-1)/2<<endl,0;
    hi=hi+hi-1;
    int h=hi/2+1;
    int ans=max(min((long long)n,hi-1)-h+1,0ll);
    for(long long hh=hi+hi+1,cnt=1;cnt<9;++cnt,hh+=hi+1){
        long long h=hh/2+1;
        ans+=max(min((long long)n,hh-1)-h+1,0ll);
    }
    cout<<ans<<endl;
}
