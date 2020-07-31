#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define pb(x) push_back(x)
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;

class MCMF{
public:
    const int INF=1e8;
    const ll LINF=1e17;
    int n;
    vector<vector<int> >res;
    vector<vector<ll> >cost;
    vector<int>p;
    vector<ll>d;
    vector<vector<int> >adj;
    MCMF(int n){
        this->n=n;
        res.assign(n,vector<int>(n));
        cost.assign(n,vector<ll>(n));
        d=vector<ll>(n);
        p=vector<int>(n);
        adj.assign(n,vector<int>());
    }
    void add_edge(int u,int v,int cap,ll _cost){
        res[u][v]+=cap;
        cost[u][v]=_cost;
        cost[v][u]=-_cost;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    pair<ll,int> aug(int u,int f){
        if(p[u]==u)return make_pair(0,f);
        pair<ll,int>_p=aug(p[u],min(f,res[p[u]][u]));
        f=min(f,_p.second);
        res[p[u]][u]-=f;
        res[u][p[u]]+=f;
        return make_pair(cost[p[u]][u]*f+_p.first,f);
    }
    pair<ll,int> go(int S,int T){
        int f=0;
        ll c=0;
        while(1){
            for(int i=0;i<n;i++)p[i]=-1;
            for(int i=0;i<n;i++)d[i]=LINF;
            set<pair<ll,int> >pq;
            pq.insert(make_pair(0,S));
            p[S]=S;
            d[S]=0;
            while((int)pq.size()){
                pair<ll,int> pr=*pq.begin();pq.erase(pq.begin());
                int u=pr.second;
                ll _cost=pr.first;
                if(_cost>d[u])continue;
                for(int v:adj[u])
                    if(res[u][v]>0&&d[v]>d[u]+cost[u][v]){
                        d[v]=d[u]+cost[u][v];
                        pq.insert(make_pair(d[v],v));
                        p[v]=u;
                    }
            }
            if(p[T]==-1)return make_pair(c,f);
            pair<ll,int>_p=aug(T,INF);
            c+=_p.first;
            f+=_p.second;
        }
    }
};

int n,k;
int left(int u){return u+1;}
int right(int u){return u+n+1;}
int src(){return 0;}
int far_sink(){return 2*n+2;}
int sink(){return 2*n+1;}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    #endif     

    scanf("%d%d",&n,&k);    
    MCMF mcmf(2*n+3);
    mcmf.add_edge(sink(),far_sink(),k,0);
    REP(i,n){
        int a;
        scanf("%d",&a);
        mcmf.add_edge(src(),left(i),1,a);
    }
    REP(i,n){
        int b;
        scanf("%d",&b);
        mcmf.add_edge(right(i),sink(),1,b);
        mcmf.add_edge(left(i),right(i),mcmf.INF,0);
        if(i!=n-1)mcmf.add_edge(right(i),right(i+1),mcmf.INF,0);
    }
    printf("%lld\n", mcmf.go(src(),far_sink()).fi);
    return 0;
}