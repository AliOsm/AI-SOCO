#include<bits/stdc++.h>
using namespace std;

double a[1005],b[1005];

int main(){
    int n; double m; cin>>n>>m;
    for(int i=1;i<=n;++i)cin>>a[i];
    for(int i=1;i<=n;++i)cin>>b[i];
    double L=0,R=1e9+87;
    while(R-L>1e-9){
        if([&](double oil)->bool{
            for(int i=1;i<=n;++i){
                oil-=(m+oil)/a[i];
                if(oil<0)return 0;
                oil-=(m+oil)/b[i%n+1];
                if(oil<0)return 0;
            }
            return 1;
        }((L+R)/2))R=(L+R)/2;
        else L=(L+R)/2;
    }
    if(L>1e9+1e-6)cout<<-1<<endl;
    else cout<<fixed<<setprecision(10)<<L<<endl;
}
