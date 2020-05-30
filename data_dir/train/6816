#include<bits/stdc++.h>
using namespace std;

int cnt[222];
int main(){
    int n,k; cin>>n>>k;
    string s; cin>>s;
    for(char c:s)++cnt[c];
    sort(cnt,cnt+222); reverse(cnt,cnt+222);
    long long ans=0;
    for(int i=0;k;++i){
        if(k>=cnt[i])ans+=cnt[i]*1ll*cnt[i],k-=cnt[i];
        else ans+=k*1ll*k,k=0;
    } cout<<ans<<endl;
}
