#include<bits/stdc++.h>
using namespace std;

int a[100005],req[100005];

int main(){
    int n; cin>>n;
    for(int i=1;i<=n;++i)cin>>a[i];
    req[n]=a[n];
    for(int i=n-1;i>=0;--i){
        req[i]=max(a[i],req[i+1]-1);
    }
    long long ans=0;
    int cnt=0;
    for(int i=1;i<=n;++i){
        if(req[i]>cnt)cnt=req[i];
        ans+=cnt-a[i]-1;
    }
    cout<<ans+n<<endl;
}
