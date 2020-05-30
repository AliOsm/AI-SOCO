/*
#####################################################
# Apparently it takes me a lot of time to win lol :(#
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
#define REP(i,n) 	    for(int i=0;i<(n);++i)
#define FOR(i,a,b)      for(int i=(a);i<(b);++i)
#define DFOR(i,a,b)     for(int i=(a);i>=(b);--i)

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
bool isPrime[1000010];
vi primes;

void sieve(){
    fill(isPrime,isPrime+1000010,true);
    isPrime[0]=isPrime[1]=false;
    REP(i,1000010)
        if(isPrime[i]){
            for(int j=2*i;j<1000010;j+=i)
                isPrime[j]=false;
            primes.pb(i);
        }
}

void getPrimeFacts(set<int> &s,int cur){
    for(int p : primes)
        if(cur%p==0){
            while(cur%p==0)
                cur/=p;
            s.insert(p);
        }

    if(cur>1)
        s.insert(cur);
}
//Main function
int main(){
    IOS;
    TIE;

    int n;
    cin>>n;

    pi arr[n];
    REP(i,n)
        cin>>arr[i].F>>arr[i].S;

    sieve();

    set<int> wcd;
    getPrimeFacts(wcd,arr[0].F);
    getPrimeFacts(wcd,arr[0].S);

    int ans=0;
    for(auto it=wcd.begin();it!=wcd.end();++it){
        int cur=*it;
        bool flag=true;
        REP(i,n)
            if(arr[i].F%cur!=0 && arr[i].S%cur!=0){
                flag=false;
                break;
            }

        if(flag){
            ans=cur;
            break;
        }
    }

    if(ans)
        cout<<ans<<endl;
    else
        cout<<-1<<endl;

    return 0;
}
