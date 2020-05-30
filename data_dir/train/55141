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
const ll mod = 998244353;
const double pi = acos(-1);
ll dp[1010][1010];
ll fixed[1010][1010];
ll power(ll n){
   if(n == 0)return 1;
   if(n == 1)return 2;
   ll p = power(n/2);
   p*=p;
   p%=mod;
   if(n%2)p*=2;
   p%=mod;
   return p;
}
int main(){
   int w,h;
   cin >> w >> h;
   ll ans = 1;
   for(int i = 1; i <= w; ++i){
      for(int j = 1; j <= h; ++j){
         int a = 1;
         if(dp[i-1][j] == 0)a*=2;
         if(dp[i][j-1] == 0)a*=2;
         dp[i][j] = a;
         ans*=dp[i][j];
         ans%=mod;
      }
   }
   cout << ans;
   return 0;
}