// #pragma GCC optimize("no-stack-protector")
// #pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
// #pragma GCC diagnostic ignored "-W"

#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<iostream>
#include<iomanip>
#include<sstream>
#include<deque>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<bitset>
#include<vector>
#include<utility>
#include<functional>
#include<complex>
#include<climits>
#include<random>
#include<thread>

#if __cplusplus >= 201103L
#include<unordered_map>
#include<unordered_set>
#include<tuple>
#endif

// #include<ext/pb_ds/assoc_container.hpp>
// #include<ext/pb_ds/tree_policy.hpp>
// #include<ext/rope>

using namespace std;
// using namespace __gnu_pbds;

#define ll long long
#define ld long double
#define X first
#define Y second
#define pb push_back
#define eb emplace_back
#define pii pair<int,int>
#define vint vector<int>
#define vpii vector<pair<int,int>>
#define SS stringstream
#define PQ priority_queue
#define MS(x,v) memset((x),(v),sizeof(x))
#define RZUNI(x) sort(x.begin(),x.end()), x.resize(unique(x.begin(),x.end())-x.begin())
#define FLH fflush(stdout)
#define CPPinput ios_base::sync_with_stdio(0); cin.tie(0)
#define FIN(fname) freopen(fname,"r",stdin)
#define FOUT(fname) freopen(fname,"w",stdout)

#define tm Ovuvuevuevue
#define y1 Enyetuenwuevue
#define left Ugbemugbem
#define ws Osas
#define dec tetteterette
#define expl explexplexpl

#define YES cout<<"YES"<<endl
#define NO cout<<"NO"<<endl
#define Yes cout<<"Yes"<<endl
#define No cout<<"No"<<endl

#ifdef WEAK
#include"/home/edison/Coding/cpp/template/debug.cpp"
#define DEB(...) printf(__VA_ARGS__),fflush(stdout)
#define WHR() printf("%s: Line %d",__PRETTY_FUNCTION__,__LINE__),fflush(stdout)
#define LOG(...) printf("%s: Line %d ",__PRETTY_FUNCTION__,__LINE__),printf(__VA_ARGS__),fflush(stdout)
#define DEBUG 1
#define exit(x) cout<<"exit code "<<x<<endl, exit(0)
#else
#define PDE(...) ;
#define DEB(...) ;
#define WHR() ;
#define LOG(...) ;
#define DEBUG 0
#endif

#define lowbit(x) ((x)&(-(x)))

void JIZZ(string output=""){cout<<output; exit(0);}

const ld PI=3.14159265358979323846264338327950288;
const ld eps=1e-10;
const ll mod=1e9+7;

vector<ll> p;
bitset<15000007> np;

void init(){
    for(int i=2;i<15000007;++i){
        if(np[i])continue;
        p.pb(i);
        for(ll j=1ll*i*i;j<15000007;j+=i){
            np[j]=1;
        }
    }
    PDE(p.size());
}

vector<ll> facs,sumfac,afac,bfac;
map<ll,int> pfac;

void dfs(map<ll,int>::iterator it,ll now){
    if(it==pfac.end()){ facs.pb(now); return; }
    auto p=*it;
    for(int z=0;z<=p.second;++z){
        dfs(next(it),now);
        now*=p.first;
    }
}

vector<ll> meow(ll x){
    facs.clear();
    pfac.clear();
    for(ll i:p){
        if(i*i>x)break;
        while(x%i==0){
            x/=i;
            ++pfac[i];
        }
    }
    if(x!=1)++pfac[x];
    dfs(pfac.begin(),1);
    sort(facs.begin(),facs.end());
    return facs;
}

#define upd() ((ans=min(ans,(mx+my)*2)));
ll go(vector<ll> &mo,vector<ll> &ch){
    ll s=mo.back(),x=ch.back();
    auto it1=mo.begin(),it2=ch.begin();
    ll ans=1e16;
    while(it1!=mo.end()){
        ll mx=*it1,my=s/(*it1);
        ll cx=*it2,cy=x/(*it2);
        if(cx<=mx && cy<=my)upd();
        while(next(it2)!=ch.end() && *next(it2)<=mx){
            ++it2;
            cx=*it2,cy=x/(*it2);
            if(cx<=mx && cy<=my)upd();
        }
        ++it1;
    }
    return ans;
}

int main(){
    CPPinput;
    init();
    ll a,b; cin>>a>>b;
    sumfac=meow(a+b);
    afac=meow(a);
    bfac=meow(b);
    PDE(sumfac,afac,bfac);
    cout<<min(go(sumfac,afac),go(sumfac,bfac))<<endl;
}
