/*
 ____________________________________________________________
|                                                            |
|                   Author: ay2306                           |
|____________________________________________________________|

*/
#include <bits/stdc++.h>
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
using namespace std;

const ll maxn = 1e5;
V<V<int> > adj;
V<bool> visited;
V<int> seq;
V<int> level;
V<int> arr;
V<ll> tree;
V<ll> lazy;
V<int> pos;
V<int> End;
int n;

void dfs(int i){
    visited[i] = true;
    seq.pb(i);
    int p = i;
    for(auto j: adj[i]){
        if(!visited[j]){
            level[j] = level[i]+1;
            dfs(j);
            p = End[j];
        }
    }
    End[i] = p;
}

void build(ll node = 0, ll start = 0, ll end = n-1){
    if(start == end){
        tree[node] = (1LL << arr[seq[start]]);
        return;
    }
    build(2*node+1, start, (start+end)/2);
    build(2*node+2, (start+end)/2+1, end);
    tree[node] = (tree[2*node+1]|tree[2*node+2]);
}

void update(ll l, ll r, ll val, ll node = 0, ll start = 0, ll end = n-1){
    if(lazy[node] != 0){
        tree[node] = lazy[node];
        if(start != end){
            lazy[2*node+1] = lazy[node];
            lazy[2*node+2] = lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > r || end < l)return;
    if(start == end){
        arr[seq[start]] = val;
        tree[node] = (1LL << val);
        if(start != end){
            lazy[2*node+1] = (1LL << val);
            lazy[2*node+2] = (1LL << val);
        }
        lazy[node] = 0;
        return;
    }
    if(l <= start && end <= r){
        tree[node] = (1LL << val);
        if(start != end){
            lazy[2*node+1] = (1LL << val);
            lazy[2*node+2] = (1LL << val);
        }
        lazy[node] = (1LL << val);
        return;
    }
    update(l,r,val,2*node+1,start,(start+end)/2);
    update(l,r,val,2*node+2,(start+end)/2+1,end);
    tree[node] = (tree[2*node+1]|tree[2*node+2]);
}

ll query(ll l, ll r, ll node = 0, ll start = 0, ll end = n-1){

    if(lazy[node] != 0){
        tree[node] = lazy[node];
        if(start != end){
            lazy[2*node+1] = lazy[node];
            lazy[2*node+2] = lazy[node];
        }
        lazy[node] = 0;
    }
    if(start > r || end < l)return 0;
    if(l <= start && end <= r){
        return tree[node];
    }
    ll p1 = query(l,r,2*node+1,start,(start+end)/2);
    ll p2 = query(l,r,2*node+2,(start+end)/2+1,end);
    return (p1|p2);
}


int main(){
    // FILE_READ_IN
    FAST
    cin >> n;
    int q;
    cin >> q;
    adj = V<V<int> > (n,V<int> ());
    visited = V<bool> (n,false);
    level = V<int> (n,0); 
    arr = V<int> (n);
    pos = V<int> (n);
    End = V<int> (n);
    tree = V<ll> (4*n);
    lazy = V<ll> (4*n,0);
    V<ll> t(n);
    loop(i,0,n){
        cin >> arr[i];
    } 
    loop(i,1,n){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].pb(b);
        adj[b].pb(a);
    }
    dfs(0);
    stack<int> s;
    unordered_map<int,PII> range;
    for(int i = 0; i < seq.size(); ++i){
        range[seq[i]] = mp(i,0);
        while(s.size() && level[s.top()] >= level[seq[i]]){
            range[s.top()].S = i-1;
            s.pop();
        }
        s.push(i);
    }
    while(s.size()){
        range[s.top()].S = n-1;
        s.pop();
    }
    loop(i,0,n){
        pos[seq[i]] = i;
    }
    build();
    while(q--){
        int t;
        cin >> t;
        if(t == 1){
            ll v,c;
            cin >> v >> c;
            ll l = pos[v-1];
            ll r = pos[End[v-1]];
            if(l > r){
                continue;
            }
            update(l,r,c);
        }else{
            ll v;
            cin >> v;
            ll l = pos[v-1];
            ll r = pos[End[v-1]];
            if(l > r){
                cout << "0\n";
                continue;
            }
            ll res = query(l,r);
            int ans = 0;
            while(res){
                ans+=(res%2);
                res/=2;
            }
            cout << ans << "\n" ;
        }
    }
    return 0;
}