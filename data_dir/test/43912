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
V<int> arr;
V<ll> dp;
ll compMax(int s){
    ll ans = LLONG_MIN;
    loop(i,0,n){
        dp[i] = arr[i];
        if(i >= s)dp[i]+=dp[i-s];
    }
    // loop(i,0,n){
    //     cout << dp[i] << " ";
    // }
    // cout << endl;
    loop(i,0,s){
        // cout << n-1-i << " " << dp[n-1-i] << "\n";
        ans=max(ans,dp[n-1-i]);
    }
    return ans;
}
int main(){
    ll ans = LLONG_MIN;
    cin >> n;
    arr = V<int> (n);
    dp = V<ll> (n);
    loop(i,0,n)cin >> arr[i];
    for(int i = 1; i*i <= n; i++){
        if(n % i)continue;
        int f1 = i;
        int f2 = n/i;
        if(f1 > 2)ans=max(compMax(f2),ans);
        if(f2 != f1 && f2 > 2)ans=max(compMax(f1),ans);
    }
    cout << ans;
   return 0;
}