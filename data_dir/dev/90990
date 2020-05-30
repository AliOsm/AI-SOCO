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

int main(){
    ll n,k;
    cin >> n >> k;
    V<ll> arr(n+1);
    V<ll> pref(n+1,0);
    loop(i,1,n+1)cin >> arr[i];
    sort(arr.begin()+1,arr.end());
    loop(i,1,n+1)pref[i] = pref[i-1]+arr[i];
    PLL ans = mp(0,0);
    loop(i,1,n+1){
        ll low = 1;
        ll high = i;
        while(low <= high){
            int mid = ((low + high) >> 1);
            ll r = i;
            ll l = i-mid+1;
            ll sum = pref[r] - pref[l-1];
            ll expectedSum = (r-l+1)*arr[i];
            ll diff = expectedSum - sum;
            if(diff <= k){
                if(mid > ans.F){
                    ans.F = mid;
                    ans.S = arr[i];
                }else if(mid == ans.F){
                    ans.S = min(ans.S,arr[i]);
                }
                low = mid+1;
            }else{
                high = mid-1;
            }
        }
    }
    cout << ans.F << " " << ans.S;
   return 0;
}