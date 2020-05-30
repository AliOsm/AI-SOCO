#include<bits/stdc++.h>
using namespace std;
#define ld long double

const ld pi=3.1415926535;
const ld eps=1e-10;

int n;
ld x[22],y[22],a[22],l,r;

ld arctan(ld t){return acos(1./sqrt(1+t*t));}
ld dp[1<<21];
ld dpf(int id){
    if(dp[id]>=-1e8)return dp[id];
    if(id==0)return l;
    for(int i=0;i<n;++i)if(id&(1<<i)){
        ld mx=dpf(id^(1<<i));
        ld dx=mx-x[i],dy=0-y[i];
        // cout<<dx<<" "<<dy<<endl;
        if(abs(dy)<eps){
            // cout<<"nody"<<endl;
            if(dx>=-eps)dp[id]=1e10;
            else dp[id]=max(dp[id],x[i]);
        }
        else if(abs(dx)<eps){
            // cout<<"nodx"<<endl;
            if(dy>=-eps)dp[id]=max(dp[id],mx-dy*tan(a[i]));
            else if(a[i]>=pi/2-eps)dp[id]=1e10;
            else dp[id]=max(dp[id],mx+abs(dy)*tan(a[i]));
        }
        else if(dx>=0){
            ld ta=atan(abs(dy/dx))-a[i];
            if(ta<=0)dp[id]=1e10;
            else dp[id]=max(dp[id],abs(dy)/tan(ta)+x[i]);
        }
        else{
            // cout<<"case"<<endl;
            ld ta=atan(abs(dx/dy))-a[i];
            // cout<<"ota: "<<atan(abs(dx/dy))<<endl;
            if(abs(ta)<eps)dp[id]=max(dp[id],x[i]);
            else if(ta>0)dp[id]=max(dp[id],x[i]-abs(dy)*tan(ta));
            else dp[id]=max(dp[id],x[i]+abs(dy)*tan(abs(ta)));
        }
    }
    return dp[id];
}

int main(){
    cin>>n>>l>>r;
    for(int i=0;i<n;++i)cin>>x[i]>>y[i]>>a[i],a[i]/=180/pi;
    for(int i=0;i<(1<<21);++i)dp[i]=-1e12;
    dpf((1<<n)-1);
    cout<<fixed<<setprecision(12)<<min(r,dpf((1<<n)-1))-l<<endl;
}
