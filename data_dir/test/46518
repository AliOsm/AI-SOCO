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
ll dp[110][110];
ll a[110];
ll b[110];
int n,m;

int main(){
    cin >> n >> m;
    loop(i,0,n){
        cin >> a[i];
    }
    loop(i,0,m){
        cin >> b[i];
    }
    loop(bit,0,35){
        V<int> A,B;
        loop(i,0,n)if((a[i]>>bit)&1LL)A.pb(i);
        loop(i,0,m)if((b[i]>>bit)&1LL)B.pb(i);
        if(abs(int(A.size()-B.size()))&1){
            cout << "NO\n";
            return 0;
        }
        if(A.size() == 0 && B.size() == 0)continue;
        if(A.size() == 0)A.pb(0);
        if(B.size() == 0)B.pb(0);
        while(B.size() > A.size()){
            dp[A.back()][B.back()]|=(1LL<<bit);
            B.pop_back();
        }
        while(B.size() < A.size()){
            dp[A.back()][B.back()]|=(1LL<<bit);
            A.pop_back();
        }
        while(A.size() && B.size()){
            dp[A.back()][B.back()]|=(1LL<<bit);
            B.pop_back();
            A.pop_back();
        }
    }
    cout << "YES\n";
    loop(i,0,n){
        loop(j,0,m)cout << dp[i][j] << " ";
        cout << "\n";
    }
   return 0;
}