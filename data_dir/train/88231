#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll a[1234];
vector<ll> na;

int main(){
    int n; cin>>n;
    ll prv; cin>>prv;
    na.push_back(prv);
    for(int i=2;i<=n;++i){
        ll nw; cin>>nw;
        if(__gcd(nw,prv)!=1){
            na.push_back(1);
        }
        na.push_back(nw);
        prv=nw;
    }
    cout<<na.size()-n<<endl;
    for(int i:na)cout<<i<<" ";
}
