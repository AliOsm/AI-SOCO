/*
#####################################################
# I will win.. maybe not immediately but definitely #
#####################################################
*/

#include <bits/stdc++.h>
using namespace std;

//Optimizations
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")

//save time
#define endl '\n'
#define db(x) cout << "> " << #x << ": " << x << endl;
typedef long long ll;

//for sorting
#define all(a) a.begin(),a.end()

//Constants
#define PI   3.141592653593
#define MOD  1000000007LL
#define EPS  0.000000001
#define INF  0X3f3f3f3f

//loops
#define REP(i,n) 	    for(ll i=0;i<(n);++i)
#define FOR(i,a,b)      for(ll i=(a);i<(b);++i)
#define DFOR(i,a,b)     for(ll i=(a);i>=(b);--i)

//vectors
#define vi vector<int>
#define vll vector<ll>
#define vii vector<pair<int,int> >
#define pb 	push_back

//pairs
#define pi pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define F first
#define S second

//fast I/O
#ifndef _WIN32
#define getchar getchar_unlocked
#define putchar putchar_unlocked
#endif
#define gc getchar
#define pc putchar
#define scan getFoo

//If using cin and cout
#define IOS ios::sync_with_stdio(false)
#define TIE cin.tie(NULL);cout.tie(NULL)

//queue
#define di deque<int>
#define dll deque<ll>
#define qi queue<int>
#define PQ priority_queue

//general
#define E empty()

//Declare all variables and methods needed between this comment and the next one(OCD lol)
ll n,s;
ll arr[100010];
ll nMax,cMin=LLONG_MAX;

void getMaxItems(ll low,ll high){
    ll mid=(low+high) >> 1;
    if(low<=high){
        ll temp[100010];
        REP(i,n)
            temp[i]=arr[i]+mid*(i+1);
        sort(temp,temp+n);

        ll tempMin=0LL;
        REP(i,mid)
            tempMin+=temp[i];
        if(nMax<mid && tempMin<=s){
            nMax=mid;
            cMin=tempMin;
        }
        else if(nMax==mid)
            cMin=min(cMin,tempMin);

        if(tempMin<=s)
            getMaxItems(mid+1,high);
        else
            getMaxItems(low,mid-1);
    }
    else
        return ;
}
//Main function
int main(){
    IOS;
    TIE;

    cin>>n>>s;
    REP(i,n)
        cin>>arr[i];

    getMaxItems(0,n);
    if(!nMax)
        cMin=0LL;

    cout<<nMax<<" "<<cMin<<endl;
    return 0;
}
