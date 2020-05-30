#include<bits/stdc++.h>
using namespace std;

struct item{
    int x,i,a,b;
} z[100005];

int main(){
    int n; cin>>n;
    for(int i=0;i<n;++i){
        z[i].i=i;
        cin>>z[i].x;
        z[i].a=z[i].b=0;
    }
    sort(z,z+n,[](const item &a,const item &b){return a.x<b.x;});
    int rep=(n-1)/3+1;
    for(int i=0;i<rep;++i){
        z[i].a=z[i].x;
    }
    for(int i=rep;i<rep*2;++i){
        z[i].b=z[i].x;
    }
    for(int i=n-1,del=1;i>=rep*2;--i,++del){
        z[i].b=del;
        z[i].a=z[i].x-del;
    }
    sort(z,z+n,[](const item &a,const item &b){return a.i<b.i;});
    cout<<"YES"<<endl;
    for(int i=0;i<n;++i)cout<<z[i].a<<" "; cout<<endl;
    for(int i=0;i<n;++i)cout<<z[i].b<<" "; cout<<endl;
}
