/*
#####################################################
# I will win.. maybe not immediately but definitely #
#####################################################
*/

#include <iostream>
#include <utility>

using namespace std;

//Optimizations
#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")

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

//Declare all variables and methods needed between this comment and the next one(OCD lol)

//Main function
int main(){
    IOS;
    TIE;

    int n;
    cin>>n;

    pi points[n];
    REP(i,n)
        cin>>points[i].F>>points[i].S;

    int cnt=0;
    for(pi p : points){
        bool flags[4]={false};
        for(auto p1 : points){
            if(p.F==p1.F){
                if(p.S<p1.S)
                    flags[0]=true;
                else if(p.S>p1.S)
                    flags[1]=true;
            }
            else if(p.S==p1.S){
                if(p.F<p1.F)
                    flags[2]=true;
                else if(p.F>p1.F)
                    flags[3]=true;
            }
        }

        bool flag=true;
        REP(i,4)
            flag &=flags[i];

        cnt+=flag;
    }

    cout<<cnt<<endl;

    return 0;
}
