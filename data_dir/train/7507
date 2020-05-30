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
char grid[510][510];
int dpHor[510][510],dpVer[510][510];
//Main function
int main(){
    IOS;
    TIE;

    int h,w;
    cin>>h>>w;

    FOR(i,1,h+1)
        FOR(j,1,w+1)
            cin>>grid[i][j];

    FOR(i,1,h+1)
        FOR(j,1,w+1)
            dpHor[i][j]=dpHor[i-1][j]+dpHor[i][j-1]-dpHor[i-1][j-1]+(grid[i][j]=='.' && grid[i][j-1]=='.');

    FOR(j,1,w+1)
        FOR(i,1,h+1)
            dpVer[i][j]=dpVer[i][j-1]+dpVer[i-1][j]-dpVer[i-1][j-1]+(grid[i][j]=='.' && grid[i-1][j]=='.');

    int q;
    cin>>q;
    REP(i,q){
        int r1,c1,r2,c2;
        cin>>r1>>c1>>r2>>c2;
        cout<<(dpHor[r2][c2]-dpHor[r2][c1]+dpHor[r1-1][c1]-dpHor[r1-1][c2])+(dpVer[r2][c2]-dpVer[r1][c2]+dpVer[r1][c1-1]-dpVer[r2][c1-1])<<endl;
    }

    return 0;
}
