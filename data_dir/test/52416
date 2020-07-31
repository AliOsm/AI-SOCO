// #pragma GCC optimize("no-stack-protector")
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

// #include<ext/pb_ds/assoc_container.hpp>
// #include<ext/pb_ds/tree_policy.hpp>

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
#define exp expexpexpexp
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

#if __cplusplus >= 201103L
#include<unordered_map>
#include<unordered_set>
#include<tuple>
#endif

void JIZZ(string output=""){cout<<output; exit(0);}

const ld PI=3.14159265358979323846264338327950288;
const ld eps=1e-13;
const ll mod=1e9+7;

struct edge{
    int u,v,w; 
};
vector<edge> edg;

// set<pair<int,int>> dp[100005];
vector<int> wono[100005];
int *bit[100005];

void add(int bid,int x,int v){
    for(;x<wono[bid].size()+5;x+=lowbit(x))bit[bid][x]=max(bit[bid][x],v);
}
int query(int bid,int x,int v=0){
    for(;x;x-=lowbit(x))v=max(v,bit[bid][x]);
    return v;
}

int main(){
    CPPinput;
    int n,m; cin>>n>>m;
    while(m--){
        int u,v,w; cin>>u>>v>>w;
        ++w;
        edg.push_back({u,v,w});
        wono[u].pb(w);
        wono[v].pb(w);
    }
    for(int i=1;i<=n;++i){
        bit[i]=new int[wono[i].size()+5];
        memset(bit[i],0,sizeof(int)*(wono[i].size()+5));
        sort(wono[i].begin(),wono[i].end());
    }
    int mx=0;
    for(auto e:edg){
        int u=e.u,v=e.v,w=e.w;
        auto upd=[&](int u,int v,int w){
            int q=query(u,lower_bound(wono[u].begin(),wono[u].end(),w)-wono[u].begin());
            ++q;
            mx=max(mx,q);
            add(v,lower_bound(wono[v].begin(),wono[v].end(),w)-wono[v].begin()+1,q);
        };
        upd(u,v,w);
        // upd(v,u,w);
    }

    cout<<mx;
}
