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
char grid[4][4];
bool check(vii v){
    int cnt=0;
    for(auto p : v)
        if(p.F>-1 && p.F<4 && p.S>-1 && p.S<4){
            if(grid[p.F][p.S]=='#')
                ++cnt;
        }
        else{
            cnt=-1;
            break;
        }

    if(cnt==0 || cnt==1 || cnt==3 || cnt==4)
        return true;
    return false;
}
//Main function
int main(){
    IOS;
    TIE;

    REP(i,4)
        REP(j,4)
            cin>>grid[i][j];

    REP(i,4)
        REP(j,4){
                vii temp;
                temp={mp(i-1,j),mp(i-1,j-1),mp(i,j-1),mp(i,j)};
                if(check(temp)){
                    cout<<"YES"<<endl;
                    return 0;
                }

                temp={mp(i-1,j),mp(i-1,j+1),mp(i,j+1),mp(i,j)};
                if(check(temp)){
                    cout<<"YES"<<endl;
                    return 0;
                }

                temp={mp(i+1,j),mp(i+1,j-1),mp(i,j-1),mp(i,j)};
                if(check(temp)){
                    cout<<"YES"<<endl;
                    return 0;
                }

                temp={mp(i+1,j),mp(i+1,j+1),mp(i,j+1),mp(i,j)};
                if(check(temp)){
                    cout<<"YES"<<endl;
                    return 0;
                }
            }

    cout<<"NO"<<endl;

    return 0;
}
