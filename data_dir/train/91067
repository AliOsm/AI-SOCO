#include<bits/stdc++.h>
using namespace std;

struct can{
    int ti,i,t;
} a[111],b[111];

int main(){
    int n,k,m,z; cin>>n>>k>>m>>z;
    int le=m-z;
    for(int i=1;i<=z;++i){
        int t; cin>>t;
        ++a[t].ti;
        a[t].t=i;
    }
    for(int i=1;i<=n;++i)a[i].i=i;
    auto cmp=[](const can &a,const can &b){return a.ti==b.ti?a.t<b.t:a.ti>b.ti;};
    sort(a+1,a+1+n,cmp);
    for(int id=1;id<=n;++id){
        int i=[&](){for(int i=1;i<=n;++i)if(a[i].i==id)return i;}();
        bool all=[&](){
            for(int i=1;i<=n;++i)b[i]=a[i];
            b[i].ti+=le;
            if(le)b[i].t=m;
            sort(b+1,b+1+n,cmp);
            return [&](){for(int z=1;z<=k;++z)if(b[z].i==id && b[z].ti>0)return 1; return 0;}();
        }(), none=[&](){
            vector<int> dk;
            for(int i=1;i<=n;++i)b[i]=a[i];
            for(int z=1;z<=n && dk.size()<k;++z)if(b[z].i!=id)dk.push_back(z);
            int u=0;
            for(int z:dk)u+=max(0,b[i].ti-b[z].ti+1-(b[z].ti==b[i].ti && b[i].t>b[z].t));
            // if(id==21)cout<<b[i].ti<<" "<<b[i].t<<" "<<u<<" "<<le<<endl;
            return b[i].ti>0 && (u>le || [&](){
                for(int z:dk)b[z].ti=b[i].ti+1;
                return sort(b+1,b+1+n,cmp),[&](){
                    for(int z=1;z<=k;++z)if(b[z].i==id && b[z].ti>0)return 1; return 0;
                }();
            }());
        }();
        // cout<<none<<endl;
        if(all && none)cout<<1<<" ";
        else if(all)cout<<2<<" ";
        else cout<<3<<" ";
    }
}
