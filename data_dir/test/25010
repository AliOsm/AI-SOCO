/*
 ____________________________________________________________
|                                                            |
|                   Author: ay2306                           |
|____________________________________________________________|

*/
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

struct oper{
    ll l;
    ll r;
    ll x;
};

V<ll> diff;
V<ll> op_diff;
V<ll> arr;

int main(){
    int n,m,k;
    cin >> n >> m >> k;
    diff = V<ll> (n);
    op_diff = V<ll> (m,0);
    arr = V<ll> (n);
    loop(i,0,n){
        cin >> arr[i];
    }
    diff[0] = arr[0];
    loop(i,1,n){
        diff[i] = arr[i]-arr[i-1];
    }
    V<oper> op(m);
    loop(i,0,m){
        cin >> op[i].l >> op[i].r >> op[i].x;
        op[i].l--;
    }
    loop(i,0,k){
        int a,b;
        cin >> a >> b;
        a--;
        op_diff[a]++;
        if(b < m){
            op_diff[b]--;
        }
    }
    V<ll> arr_op(m,0);
    arr_op[0] = op_diff[0];
    loop(i,1,m){
        arr_op[i] = arr_op[i-1] + op_diff[i];
    }
    loop(i,0,m){
        op[i].x*=arr_op[i];
        diff[op[i].l]+=op[i].x;
        if(op[i].r < n){
            diff[op[i].r]-=op[i].x;
        }
    }
    arr[0] = diff[0];
    loop(i,1,n){
        arr[i] = arr[i-1] + diff[i];
    }
    loop(i,0,n){
        cout << arr[i] << " ";
    }
    return 0;
}