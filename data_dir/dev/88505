#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define pb(x) push_back(x)
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define double long double
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;


ll odd(ll a,ll b){
    return (b+1)/2-a/2;
}
ll even(ll a,ll b){
    return b/2-(a-1)/2;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll x1,y1,x2,y2;
    cin>>x1>>y1>>x2>>y2;
    if((x1+y1)&1)x1++,x2++;
    ll add=1e9+2;
    x1+=add;
    y1+=add;
    x2+=add;
    y2+=add;
    ll c1=(x2-x1)/2+1,c2=(x2-x1)/2;
    if(x1&1ll)c1*=odd(y1,y2);
    else c1*=even(y1,y2);
    
    if((x1+1)&1ll)c2*=odd(y1,y2);
    else c2*=even(y1,y2);
    cout<<c1+c2<<"\n";
}