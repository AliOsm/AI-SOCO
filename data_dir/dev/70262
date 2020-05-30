#include<bits/stdc++.h>
using namespace std;
int a[2005];

int main(){
    int n,g=0,c1=0; cin>>n; bool all1=1;
    for(int i=0;i<n;++i)cin>>a[i],all1&=a[i]==1,g=__gcd(g,a[i]),c1+=a[i]==1;
    if(all1)return cout<<0<<endl,0;
    if(g!=1)return cout<<-1<<endl,0;
    if(c1)return cout<<n-c1<<endl,0;
    int mn=987987;
    for(int i=0;i<n;++i){
        for(int j=i+1;j<n;++j){
            a[i]=__gcd(a[i],a[j]);
            if(a[i]==1){mn=min(mn,j-i); break;}
        }
    }
    cout<<mn+n-1<<endl;
}
