#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll dp[2][150006];

int main(){
    int n,m,d; cin>>n>>m>>d;
    ll prvt=-9999999;
    for(int $=1;$<=m;++$){
        // cout<<"now $="<<$<<endl;

        ll a,b,t; cin>>a>>b>>t;
        ll move=(t-prvt)*d;
        prvt=t;
        deque<int> dq;
        for(int i=1;i<=move && i<=n;++i){
            while(dq.size() && dp[$&1^1][dq.back()]<=dp[$&1^1][i])dq.pop_back();
            dq.push_back(i);
        }

        for(int i=1;i<=n;++i){
            if(i+move<=n){
                while(dq.size() && dp[$&1^1][dq.back()]<=dp[$&1^1][i+move])dq.pop_back();
                dq.push_back(i+move);
            }
            dp[$&1][i]=dp[$&1^1][dq.front()]+b-abs(a-i);
            // cout<<"dp["<<$<<"]["<<i<<"] from "<<dq.front()<<" : "<<dp[$-1][dq.front()]<<" , dp="<<dp[$][i]<<endl;
            if(dq.front()==i-move)dq.pop_front();
        }
    }
    ll mx=-(1ll<<62);
    for(int i=1;i<=n;++i)mx=max(mx,dp[m&1][i]);
    cout<<mx<<endl;
}
