//Strike me down and I shall become stronger, than you can possibly imagine
//Streak Count : 0
#include <bits/stdc++.h>
using namespace std;

//save time
#define endl '\n'
typedef long long ll;

//for sorting
#define all(a) a.begin(),a.end()

//Constants
#define PI   3.141592653593
#define MOD  1000000007LL
#define EPS  0.000000001

//loops
#define REP(i,n) 	    for(ll i=0;i<(n);++i)
#define FOR(i,a,b)      for(ll i=(a);i<(b);++i)
#define DFOR(i,a,b)     for(ll i=(a);i>=(b);--i)

//vectors
#define vi vector<int>
#define vll vector<ll>
#define vii vector<pair<int,int> >
#define pb 	push_back
#define pf push_front

//pairs
#define pi pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define F first
#define S second

//general
#define E empty()

//Variables and Functions required
map<string,int> cnt;
//Main function
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin>>n;
    int arr[n];
    REP(i,n)
        cin>>arr[i];
    int maxIdx=0,maxVal=arr[0];
    REP(i,n)
        if(maxVal<arr[i]){
            maxVal=arr[i];
            maxIdx=i;
        }
    int minIdx=n-1,minVal=arr[n-1];
    DFOR(i,n-1,0)
        if(minVal>arr[i]){
            minVal=arr[i];
            minIdx=i;
        }
    int ans=n-1-minIdx+maxIdx;
    if(maxIdx>minIdx)
        --ans;
    cout<<ans<<endl;
    return 0;
}
