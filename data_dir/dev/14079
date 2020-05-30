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
using namespace std;
// For ordered_set
using namespace __gnu_pbds;
template <typename T>
using ord_set = tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>;
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);
int n;
ll arr[maxn*2+10];
ll sarr[maxn*2+10];
void solve(){
   ll p,k;
   cin >> n >> p >> k;
   ll dp[n+1][2];
   loop(i,1,n+1)cin >> arr[i];
   loop(i,1,n+1)sarr[i]+=sarr[i-1];
   sort(arr+1,arr+n+1);
   int ans = 0;
   dp[0][0] = 0;
   dp[0][1] = 0;
   loop(i,1,n+1){
      dp[i][0] = min(dp[i-1][0],dp[i-1][1]) + arr[i];
      if(i >= k)dp[i][1] = min(dp[i-k][0],dp[i-k][1])+arr[i];
      else dp[i][1] = inf;
      if(dp[i][0] <= p || dp[i][1] <= p){
         ans = i;
      }
   }
   cout << ans << "\n";
}

int main(){
   FAST
   int t = 0;
   cin >> t;
   while(t--){
       solve();
   }
   return 0;
}