/*
 ____________________________________________________________
|                                                            |
|                   Author: ay2306                           |
|____________________________________________________________|

*/
#include <bits/stdc++.h>
#define MOD 1000000007
#define test int t; cin>>t; while(t--)
#define init(arr,val) memset(arr,val,sizeof(arr))
#define loop(i,a,b) for(int i=a;i<b;i++)
#define loopr(i,a,b) for(int i=a;i>=b;i--)
#define loops(i,a,b,step) for(int i=a;i<b;i+=step)
#define looprs(i,a,b,step) for(int i=a;i>=b;i-=step)
#define ull unsigned long long int
#define ll long long int
#define P pair
#define PLL pair<long long, long long>
#define PII pair<int, int>
#define PUU pair<unsigned long long int, unsigned long long int>
#define L list
#define V vector
#define D deque
#define ST set
#define MS multiset
#define M map
#define UM unordered_map
#define mp make_pair
#define pb push_back
#define pf push_front
#define MM multimap
#define F first
#define S second
#define IT iterator
#define RIT reverse_iterator
#define FAST ios_base::sync_with_stdio(false);cin.tie();cout.tie();
#define FILE_READ_IN freopen("input.txt","r",stdin);
#define FILE_READ_OUT freopen("output.txt","w",stdout);
using namespace std;

const ll N = 3010;
const ll INF = 1e9;
bool visited[N][N];
vector<int> adj[N];
int n,m,k,dist[N][N];
set<PII> cant[N];

void bfs(int s){
    queue<PII> q;
    q.push(mp(s,s));
    dist[s][s] = 0;
    while(q.size()){
        int par = q.front().first;
        int gpar = q.front().second;
        q.pop();
        for(auto &cur: adj[par]){
            if(visited[par][cur])continue;
            if(cant[gpar].find(mp(par,cur)) != cant[gpar].end())continue;
            dist[par][cur] = dist[gpar][par] + 1;
            q.push(mp(cur,par));
            visited[par][cur] = true;
        }
    }
}

int main(){
    cin >> n >> m >> k;
    loop(i,0,m){
        int a,b;
        cin >> a >> b;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    loop(i,0,k){
        int a,b,c;
        cin >> a >> b >> c;
        cant[a].insert(mp(b,c));
    }
    bfs(1);
    int d = INF;
    for(int i = 1; i <= n; ++i){
        if(dist[i][n] != 0){
            d = min(d,dist[i][n]);
        }
    }
    if(d == INF){
        cout << "-1";
        return 0;
    }
    stack<int> route;
    route.push(n);
    while(route.top()!=1){
        int cur = route.top();
        for(int i = 1; i <= n; ++i){
            if(dist[i][cur] == d){
                route.push(i);
                break;
            }
        }
        d--;
    }
    cout << route.size()-1 << "\n";
    while(route.size()){
        cout << route.top() << " ";
        route.pop();
    }
    return 0;
}