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

V<int> p;
V<int> r;

int fp(int x){
    while(p[x] != x){
        p[x] = p[p[x]];
        x = p[x];
    }
    return x;
}

void u(int a,int b){
    a = fp(a);
    b = fp(b);
    if(r[a] < r[b]){
        p[a] = b;
    }else{
        p[b] = p[a];
        if(r[a] == r[b])r[a]++;
    }
}

int main(){
    int n,m;
    cin >> n >> m;
    if(m != n-1){
        while(m--){
            int a,b;
            cin >> a >> b;
        }
        cout << "no";
        return 0;
    }
    p = V<int> (n,0);
    r = V<int> (n,0);
    loop(i,0,n)p[i] = i;
    while(m--){
        int a,b;
        cin >> a >> b;
        a--;
        b--;
        u(a,b);
    }
    unordered_map<int,int> k;
    loop(i,0,n){
        k[fp(i)]++;
    }
    if(k.size() == 1){
        cout << "yes";
        return 0;
    }
    cout << "no";
    return 0;
}