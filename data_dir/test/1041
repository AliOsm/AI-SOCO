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
const ll N = 5e6 + 10;
int arr[N];
int a[N];
int main(){
    for(int i = 2; i < N; ++i){
        if(arr[i] == 0){
            for(int j = 1; i*j < N; ++j){
                arr[i*j] = i;
            }
        }
    }
    loop(i,2,N){
        a[i] = a[i/arr[i]] + 1;
    }
    loop(i,0,N){
        a[i]+=a[i-1];
    }
    int t;
    scanf("%d",&t);
    loop(k,0,t){
        int x,y;
        scanf("%d%d",&x,&y);
        printf("%d\n",a[x]-a[y]);
    }
    return 0;
}