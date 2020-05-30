#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define ld long double

int main(){
    ll h,w,ah=0,aw=0; cin>>h>>w;
    auto up=[&](ll h,ll w){
        if(aw*ah>h*w)return;
        if(aw*ah==h*w){
            if(ah>h)return;
        }
        ah=h, aw=w;
    };
    [=,&ah,&aw]()mutable{
        while((h&-h)!=h)h-=(h&-h);
        while(h){
            ll wmx=floor(1.25*h);
            ll wmn=ceil(0.8*h-1e-12);
            if(wmx>=w && w>=wmn)up(h,w);
            if(w>=wmx)up(h,wmx);
            h>>=1;
        }
    }();
    [=,&ah,&aw]()mutable{
        while((w&-w)!=w)w-=(w&-w);
        while(w){
            ll hmx=floor(1.25*w);
            ll hmn=ceil(0.8*w-1e-12);
            if(hmx>=h && h>=hmn)up(h,w);
            if(h>=hmx)up(hmx,w);
            w>>=1;
        }
    }();
    cout<<ah<<" "<<aw<<endl;
}
