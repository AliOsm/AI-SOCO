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

int n;

ll ncr(ll n,ll r){
    ll res=1;
    REP(i,r)
        res=res*(n-i)/(i+1);
    return res;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin>>n;
    cout<<ncr(5+n-1,5)*ncr(3+n-1,3)<<"\n";
}