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
    FAST
    string a[3];
    loop(i,0,3)cin >> a[i];
    unordered_map<char,int> m[3];
    loop(j,0,3)for(auto &i: a[j])m[j][i]++;
    PII ans = {0,0};
    loop(b,0,a[0].length()+1){
        bool imp = true;
        int a_min = a[0].length();
        for(auto &i: m[1])imp=(imp&&(m[0][i.F]-(i.S*b) >= 0));
        for(auto &i: m[2])a_min=min(a_min,max(0,(m[0][i.F]-(m[1][i.F]*b))/i.S));
        if(imp && a_min+b > ans.F+ans.S)ans={b,a_min};
        if(!imp)break;
    }
    // cout << ans.F << " " << ans.S << "\n";
    for(auto &i: m[1])m[0][i.F]-=(ans.F*i.S);
    for(auto &i: m[2])m[0][i.F]-=(ans.S*i.S);
    string ans1 = "";
    loop(i,0,ans.F)cout << a[1];
    loop(i,0,ans.S)cout << a[2];
    for(auto &i: m[0])cout << string(i.S,i.F);
   return 0;
}