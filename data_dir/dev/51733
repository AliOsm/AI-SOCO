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

void solve(){
   unordered_map<int,int> m;
   int n,k;
   cin >> n >> k;
   V<int> arr(n),dem(k);
   loop(i,0,n){
      cin >> arr[i];
   }
   loop(i,0,k)cin >> dem[i];
   int st = 0;
   ll ans = 0;
   int j = 0;
   loop(i,0,k){
      if(m.find(dem[i]) != m.end()){
         ans++;
         st--;
      }else{
         ans+=st;
         while(j < n && arr[j] != dem[i]){
            m[arr[j]]++;
            st++;
            ans++;
            j++;
         }
         j++;
         ans+=st;
         ans++;
      }
      // printf("i = %d, ans = %lld\n",i,ans);
   }
   cout << ans << "\n";
}

int main(){
   int t;
   cin >> t;
   while(t--)solve();
   return 0;
}