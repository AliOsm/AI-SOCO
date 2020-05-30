/*
#####################################################
# I will win.. maybe not immediately but definitely #
#####################################################
*/

#include <bits/stdc++.h>
using namespace std;

//Optimizations
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")

//save time
#define endl '\n'
#define db(x) cout << "> " << #x << ": " << x << endl;
typedef long long ll;

//for sorting
#define all(a) a.begin(),a.end()

//Constants
#define PI   3.141592653593
#define MOD  1000000007LL
#define EPS  0.000000001
#define INF  0X3f3f3f3f

//loops
#define REP(i,n) 	    for(ll i=0;i<(n);++i)
#define FOR(i,a,b)      for(ll i=(a);i<(b);++i)
#define DFOR(i,a,b)     for(ll i=(a);i>=(b);--i)

//vectors
#define vi vector<int>
#define vll vector<ll>
#define vii vector<pair<int,int> >
#define pb 	push_back

//pairs
#define pi pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define F first
#define S second

//fast I/O
#ifndef _WIN32
#define getchar getchar_unlocked
#define putchar putchar_unlocked
#endif
#define gc getchar
#define pc putchar
#define scan getFoo

//If using cin and cout
#define IOS ios::sync_with_stdio(false)
#define TIE cin.tie(NULL);cout.tie(NULL)

//queue
#define di deque<int>
#define dll deque<ll>
#define qi queue<int>
#define PQ priority_queue

//general
#define E empty()

//Declare all variables and methods needed between this comment and the next one(OCD lol)
ll n,m;
vector<pll> adj[100010];
bool marked[100010];
ll minDist[100010];
ll prevIdx[100010];
dll dijkstra(){
    fill(minDist,minDist+100010,LLONG_MAX);

    PQ<pll,vector<pll>,greater<pll>> q;
    minDist[1]=0LL;
    q.push(mp(minDist[1],1LL));
    while(!q.E){
        ll cur=q.top().S;
        q.pop();
        marked[cur]=true;

        for(auto p : adj[cur])
            if(!marked[p.F] && minDist[p.F]>minDist[cur]+p.S){
                prevIdx[p.F]=cur;
                minDist[p.F]=p.S+minDist[cur];
                q.push(mp(minDist[p.F],p.F));
            }
    }

    ll curIdx=n;
    dll ans;
    if(minDist[n]==LLONG_MAX)
        ans.push_front(-1LL);
    else
        while(curIdx){
            ans.push_front(curIdx);
            curIdx=prevIdx[curIdx];
        }

    return ans;
}
//Main function
int main(){
    IOS;
    TIE;

    cin>>n>>m;

    map<pll,ll> edges;
    REP(i,m){
        ll v1,v2,w;
        cin>>v1>>v2>>w;

        if(v1==v2)
            continue;
        else if(edges[mp(min(v1,v2),max(v1,v2))])
            edges[mp(min(v1,v2),max(v1,v2))]=min(edges[mp(min(v1,v2),max(v1,v2))],w);
        else
            edges[mp(min(v1,v2),max(v1,v2))]=w;
    }

    for(auto it=edges.begin();it!=edges.end();++it){
        adj[it->F.F].pb(mp(it->F.S,it->S));
        adj[it->F.S].pb(mp(it->F.F,it->S));
    }

    dll ans=dijkstra();
    for(ll x : ans)
        cout<<x<<" ";
    cout<<endl;

    return 0;
}
