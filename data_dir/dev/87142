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
ll dp[5010][5010];
int main(){
    ll n,a,b,k;
    cin >> n >> a >> b >> k;
    if(a > b){
        a = n-a+1;
        b = n-b+1;
    }
    dp[a][0] = 1;
    // loop(i,1,b){
    //     printf("%3lld ",dp[i][0]);
    // }
    // printf("\n");
    loop(j,1,k+1){
        loop(i,1,b){
            dp[i][j-1]+=dp[i-1][j-1];
            while(dp[i][j] < 0)dp[i][j-1]+=MOD;
            if(dp[i][j] >= MOD)dp[i][j-1]%=MOD;
        }
        loop(i,1,b){
            int diff = (b-i);
            if(diff&1)diff/=2;
            else diff = (diff>>1)-1;
            dp[i][j] = dp[i-1][j-1] + (dp[i+diff][j-1]-dp[i][j-1]);
            while(dp[i][j] < 0)dp[i][j]+=MOD;
            if(dp[i][j] >= MOD)dp[i][j]%=MOD;
        }
        // loop(i,1,b){
        //     printf("%3lld ",dp[i][j]);
        // }
        // printf("\n");
    }
    ll ans = 0;
    loop(i,1,b){
        ans+=dp[i][k];
        if(ans >= MOD)ans-=MOD;
    }
    cout << ans;
   return 0;
}