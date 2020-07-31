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
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);
const int N = 110;
int dp[N][N][N];
void solve(){
   FAST
   int n;
   cin >> n;
   V<int> arr(n+1);
   int odd = n/2+(n%2);
   int even = n/2;
   int last = -1;
   int last_index = -1;
   int f = -1;
   int l = -1;
   V<int> a[3];
   loop(i,0,n){
      cin >> arr[i];
      if(arr[i] > 0){
         int s = (arr[i]&1);
         if(s)odd--;
         else even--;
         if(last == -1){
            f = i;
         }else{
            s+=(arr[last]&1);
            a[s].pb(i-last-1);
         }
         last = i;
      }
      // if(i == n-1){
      //    if(arr[i] == 0){
      //       l = last;

      //    }else{}
      // }
   }
   if(n == 1){
      cout << "0";
      return ;
   }else if(odd+even == n){
      cout << 1;
      return ;
   }
   sort(all(a[0]),greater<int>());
   sort(all(a[1]),greater<int>());
   sort(all(a[2]),greater<int>());
   int ans = 0 ;
   loopr(i,n-1,0){
      if(arr[i] != 0){
         l = i;
         break;
      }
   }
   while(a[0].size()){
      int i = a[0].back();
      if(i > 0){
         // printf("EVEN %d, even = %d\n",i,even);
         if(even >= i)even-=i;
         else{
            ans+=(2*a[0].size());
            break;
         }
      }
      a[0].pop_back();
   }
   while(a[2].size()){
      int i = a[2].back();
      if(i > 0){
         // printf("ODD %d, odd = %d\n",i,odd);
         if(odd >= i)odd-=i;
         else{
            ans+=(2*a[2].size());
            break;
         }
      }
      a[2].pop_back();
   }
   V<PLL> op;
   op.pb({f,arr[f]});
   if(l != -1)op.pb({n-1-l,arr[l]});
   sort(all(op));
   for(auto i: op){
      if(i.F == 0)continue;
      // cout << i.F << "\n";
      if(i.S&1){
         if(odd < i.F)ans++;
         else odd-=i.F;
      }
      else{
         if(even < i.F)ans++;
         else even-=i.F;
      }
   }
   cout << ans+a[1].size();
}

int main(){
   int t = 1;
//    cin >> t;
   while(t--){
       solve();
   }
   return 0;
}