#include <bits/stdc++.h>
//For ordered_set
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
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
#define RIT reverse_itertor
#define FAST ios_base::sync_with_stdio(false);cin.tie();cout.tie();
#define FILE_READ_IN freopen("input.txt","r",stdin);
#define FILE_READ_OUT freopen("output.txt","w",stdout);
#define all(a) a.begin(),a.end()
using namespace std;
// For ordered_set
// using namespace __gnu_pbds;
// template <typename T>
// using ord_set = tree<T,null_type,less<T>,rb_tree_tag,tree_order_statistics_node_update>;
const ll maxn = 1e5;
const ll inf = 1e9;
const double pi = acos(-1);
int n,m;
V<V<int>> adj;
V<int> level;
V<ll> arr;
V<int> start;
V<int> discover;
V<int> finish;
V<ll> tree;
V<ll> lazy;

void update(int l, int r, int val, int node = 0, int start = 0, int end = arr.size()-1){
    if(lazy[node] != 0){
        tree[node]+=lazy[node];
        if(start != end){
            lazy[2*node+1]+=lazy[node];
            lazy[2*node+2]+=lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > r || end < l)return;
    if(l <= start && end <= r){
        tree[node]+=val;
        if(start != end){
            lazy[2*node+1]+=val;
            lazy[2*node+2]+=val;
        }
        return;
    }
    update(l,r,val,2*node+1,start,((start+end)>>1));
    update(l,r,val,2*node+2,((start+end)>>1)+1,end);
    tree[node] = tree[2*node + 1] + tree[2*node+2];
}

ll query(int l, int r, int node = 0, int start = 0, int end = arr.size()-1){
    if(lazy[node] != 0){
        tree[node]+=lazy[node];
        if(start != end){
            lazy[2*node+1]+=lazy[node];
            lazy[2*node+2]+=lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > r || end < l)return 0;
    if(l <= start && end <= r){
        return tree[node];
    }
    return query(l,r,2*node+1,start,((start+end)>>1)) + query(l,r,2*node+2,((start+end)>>1)+1,end);
}

int counter = 0;

void setDfs(int s = 0, int parent = -1){
    discover.pb(s);
    start[s] = counter;
    if(parent == -1)level[s] = 0;
    else level[s] = level[parent]+1;
    for(int &i: adj[s]){
        if(i == parent)continue;
        counter++;
        setDfs(i,s);
    }
    finish[s] = counter;
}

int main(){
    FAST
    cin >> n >> m;
    adj = V<V<int>> (n);
    arr = V<ll> (n);
    tree = V<ll> ((n << 2),0);
    lazy = V<ll> ((n << 2),0);
    level = V<int> (n);
    start = V<int> (n);
    finish = V<int> (n);
    level = V<int> (n);
    loop(i,0,n)cin >> arr[i];
    loop(i,0,n-1){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    // setLevel();
    counter = 1;
    setDfs();
    // printf("Structure of node 6 = ");
    // for(int i = start[5]-1; i <= finish[5]-1; ++i)printf("%d ",discover[i]+1);
    while(m--){
        int t;
        cin >> t;
        if(t == 1){
            int x;
            ll val;
            cin >> x >> val;
            x--;
            if(level[x] & 1){
                update(start[x]-1,finish[x]-1,val);
            }else{
                update(start[x]-1,finish[x]-1,-val);
            }
        }else{
            int x;
            cin >> x;
            x--;
            if(level[x] & 1){
                ll change = query(start[x]-1,start[x]-1);
                cout << arr[x]+change << "\n";
            }else{
                ll change = query(start[x]-1,start[x]-1);
                cout << arr[x]-change << "\n";
            }
        }
    }
   return 0;
}