/*
#####################################################
# I will win.. maybe not immediately but definitely #
#####################################################
*/

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
#define REP(i,n) 	    for(int i=0;i<(n);++i)
#define FOR(i,a,b)      for(int i=(a);i<(b);++i)
#define DFOR(i,a,b)     for(int i=(a);i>=(b);--i)

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
#define qi queue<int>
#define PQ priority_queue

//general
#define E empty()

//Input methods
template <typename T>
void getFoo(T &x){
    x=0;
    register char c=gc();
    for(;c<48 || c>57;c=gc());
    for(;c>47 && c<58;c=gc())
        x=(x<<1)+(x<<3)+c-48;
}

template <typename T1,typename T2>
void getFoo(T1 &x,T2 &y){
    getFoo(x);
    getFoo(y);
}

template <typename T1,typename T2,typename T3>
void getFoo(T1 &x,T2 &y,T3 &z){
    getFoo(x);
    getFoo(y);
    getFoo(z);
}
//Declare all variables and methods needed between this comment and the next one(OCD lol)
bool isPrime[1000010];
vll primes;

void sieve(){
    fill(isPrime+2,isPrime+1000010,true);

    FOR(i,2,1000010)
        if(isPrime[i]){
            primes.pb(i);
            for(int j=2*i;j<1000010;j+=i)
                isPrime[j]=false;
        }
}

//Main function
int main(){
    IOS;
    TIE;

    int n,m;
    cin>>n>>m;

    sieve();

    ll mtrx[n][m];
    REP(i,n)
        REP(j,m)
            cin>>mtrx[i][j];

    ll minCnt=LLONG_MAX;
    REP(i,n){
        ll tempCnt=0;
        REP(j,m)
            if(!isPrime[mtrx[i][j]])
                tempCnt+=*upper_bound(all(primes),mtrx[i][j])-mtrx[i][j];

        minCnt=min(minCnt,tempCnt);
    }

    REP(j,m){
        ll tempCnt=0;
        REP(i,n)
            if(!isPrime[mtrx[i][j]])
                tempCnt+=*upper_bound(all(primes),mtrx[i][j])-mtrx[i][j];

        minCnt=min(minCnt,tempCnt);
    }

    cout<<minCnt<<endl;

    return 0;
}
