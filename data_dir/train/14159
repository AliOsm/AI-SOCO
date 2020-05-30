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

const ll maxn = 1e5;

int n,m;
V<V<int> > adj;
V<PII> edges;
V<bool> visited;
V<int> color;
bool colorpos;

void dfs(int s = 1, int col = 1){
  visited[s] = true;
  color[s] = col;
  for(auto i: adj[s]){
    if(!visited[i])dfs(i,1-col);
    else if(color[i] == col)colorpos = false;
  }
}

int main(){
    cin >> n >> m;
    adj = V<V<int> > (n+1);
    edges = V<PII> ();
    visited = V<bool>(n+1,false);
    color = V<int> (n+1,-1);
    loop(i,0,m){
      int a,b;
      cin >> a >> b;
      adj[a].pb(b);
      adj[b].pb(a);
      edges.pb(mp(a,b));
    }
    colorpos = true;
    dfs();
    if(!colorpos){
      cout << "NO\n";
      return 0;
    }
    string ans = "";
    for(auto i:edges){
      if(color[i.F] == color[i.S]){
        // printf("(%d, %d)  ",i.F,i.S);
        cout << "NO\n";
        return 0;
      }
      if(color[i.F]){
        ans+="1";
      }else{
        ans+="0";
      }
    }
    cout << "YES\n";
    cout << ans;
    return 0;
}
