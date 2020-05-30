#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll sz[100];
ll offset[100];

int main(){
    ios_base::sync_with_stdio(0); cin.tie(0);
    sz[1]=1;
    for(int i=2;i<100;++i)sz[i]=sz[i-1]*2;
    int q; cin>>q; while(q--){
        int t; cin>>t;
        if(t==1){
            ll x,k; cin>>x>>k;
            int lvl=0;
            while(x)x>>=1,++lvl;
            k=sz[lvl]-k;
            offset[lvl]+=k;
        }
        else if(t==2){
            ll x,k; cin>>x>>k;
            int lvl=0;
            while(x)x>>=1,++lvl;
            k=sz[lvl]-k;
            for(;lvl<65;++lvl){
                offset[lvl]+=k;
                k<<=1;
            }
        }
        else{
            ll x; cin>>x;
            int lvl=[x]()mutable{int rt=0; while(x)x>>=1,++rt; return rt;}();
            x=((x-offset[lvl])%sz[lvl]+sz[lvl])%sz[lvl]+sz[lvl];
            while(x){
                cout<<((x+offset[lvl])%sz[lvl]+sz[lvl])%sz[lvl]+sz[lvl]<<" ";
                --lvl; x>>=1;
            }
            cout<<'\n';
        }
    }
}
