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
#define MAX(x,y) (x>y)?x:y
#define MIN(x,y) (x<y)?x:y
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
ll dp[2010][2010];
//Main function
int main(){
    IOS;
    TIE;

    int n,m;
    cin>>n>>m;

    string str;
    cin>>str;

    ll openCnt=0,closeCnt=0,balance=LLONG_MIN;
    REP(i,m){
        if(str[i]=='(')
            ++openCnt;
        else
            ++closeCnt;
        balance=MAX(balance,closeCnt-openCnt);
    }

    dp[0][0]=1;
    FOR(i,1,n-m+1)
        REP(j,i+1){
            if(j)
                dp[i][j]+=dp[i-1][j-1];
            dp[i][j]+=dp[i-1][j+1];
            dp[i][j]%=MOD;
        }

    ll ans=0;
    REP(i,n-m+1)
        FOR(j,MAX(0,balance),i+1)
            if(openCnt-closeCnt+j>n-m-i)
                break;
            else
                ans=(ans+(dp[i][j]*dp[n-m-i][j+openCnt-closeCnt])%MOD)%MOD;
    cout<<ans<<endl;

    return 0;
}
