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
#define FILE_READ freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#define MAXN 25
using namespace std;

ll readInt () {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
 
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
 
	if (ch == '-') minus = true; else result = ch-'0';
 
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
 
	if (minus)
		return -result;
	else
		return result;
 
}
int main(){
    int n =readInt();
    int m = readInt();
    int tm = m;
    int mn = INT_MAX, mx = INT_MIN;
    int *arr = new int[n];
    loop(i,0,n){
        arr[i] = readInt();
        mn = min(mn,arr[i]);
        mx = max(mx,arr[i]);
    }
    loop(i,0,n){
        // printf("arr[%d] = %d and mx = %d and mx-arr[%d] = %d\n",i,arr[i],mx,i,mx-arr[i]);
        arr[i] = mx-arr[i];
        tm-=arr[i];
        // printf("tm = %d\n",tm);
    }
    // printf("Final tm = %d\n",tm);
    cout << mx+ ((tm > 0)?((tm/n)+ ((tm%n)?1:0)):0)  << " " << mx + m;
    return 0;
}

// 10 20 80 41 15 77 91 82 15 83 36 3