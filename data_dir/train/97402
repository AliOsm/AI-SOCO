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
#define vii vector<pair<int,int>>
#define vlll vector<pair<ll,ll>>
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
ll dp[200010][2];
//Main function
int main(){
    IOS;
    TIE;

    ll r,g;
    cin>>r>>g;

    ll maxH=0;
    REP(i,1000)
        if(i*(i+1)/2>r+g){
            maxH=i-1;
            break;
        }

    dp[0][0]=1;
    FOR(h,1,maxH+1){
        ll curBlocks=h*(h+1)/2;

        FOR(i,h,min(curBlocks,r)+1)
            dp[i][h&1]=(dp[i-h][~h&1]+dp[i][h&1])%MOD;

        FOR(i,max(0LL,curBlocks-g),min(r,curBlocks-h)+1)
            dp[i][h&1]=(dp[i][~h&1]+dp[i][h&1])%MOD;

        REP(i,r+1)
            dp[i][~h&1]=0;
    }

    ll sum=0;
    REP(i,r+1)
        sum=(sum+dp[i][maxH&1])%MOD;

    cout<<sum<<endl;
    
    return 0;
}
