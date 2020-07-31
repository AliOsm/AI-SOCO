#include <bits/stdc++.h>
//For ordered_set
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
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
#define all(a) a.begin(),a.end()
#define ld long double
using namespace std;
// For ordered_set
using namespace __gnu_pbds;
template <typename T>
using ord_set = tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>;
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);
int n;
V<V<int>> adj;
V<int> color;
V<int> arr;
void make_linear(int s, int p = -1){
   arr.pb(s);
   for(int i : adj[s]){
      if(i != p)make_linear(i,s);
   }
}

int main(){
   FAST
   cin >> n;
   adj = V<V<int>> (n);
   color = V<int> (n,-1);
   V<ll> costs[3];
   loop(i,0,3){
      ll a;
      loop(j,0,n){
         cin >> a;
         costs[i].pb(a);
      }
   }
   loop(i,1,n){
      int a,b;
      cin >> a >> b;
      a--;
      b--;
      adj[a].pb(b);
      adj[b].pb(a);
   }
   loop(i,0,n){
      if(adj[i].size() > 2){
         cout << "-1";
         return 0;
      }
   }
   loop(i,0,n){
      if(adj[i].size() == 1){
         make_linear(i);
         break;
      }
   }
   V<int> bestColors(n);
   ll finalCost = LLONG_MAX;
   int perm[3] = {0,1,2};
   do{
      ll cost = 0;
      loop(i,0,n){
         cost+=costs[perm[i%3]][arr[i]];
      }
      if(cost < finalCost){
         finalCost = cost;
         loop(i,0,n){
            bestColors[arr[i]]=perm[i%3]+1;
         }
      }
   }while(next_permutation(perm,perm+3));
   cout << finalCost << "\n";
   loop(i,0,n){
      cout << bestColors[i] << " ";
   }
   return 0;
}