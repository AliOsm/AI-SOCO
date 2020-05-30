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
vll teamA,teamB;
vll cntA,cntB;

ll binarySearchA(ll low,ll high,ll key){
    ll mid=(low+high) >> 1;
    if(low>high)
        return mid;
    else{
        if(teamA[mid]>key)
            return binarySearchA(low,mid-1,key);
        else if(teamA[mid]==key)
            return mid;
        else
            return binarySearchA(mid+1,high,key);
    }
}

ll binarySearchB(ll low,ll high,ll key){
    ll mid=(low+high) >> 1;
    if(low>high)
        return mid;
    else{
        if(teamB[mid]>key)
            return binarySearchB(low,mid-1,key);
        else if(teamB[mid]==key)
            return mid;
        else
            return binarySearchB(mid+1,high,key);
    }
}
//Main function
int main(){
    IOS;
    TIE;

    ll n;
    cin>>n;

    map<ll,ll> aMap;
    REP(i,n){
        int temp;
        cin>>temp;
        ++aMap[temp];
    }
    teamA.pb(0);
    cntA.pb(0);
    for(auto it=aMap.begin();it!=aMap.end();++it){
        teamA.pb(it->F);
        cntA.pb(it->S+cntA.back());
    }

    ll m;
    cin>>m;

    map<ll,ll> bMap;
    REP(i,m){
        int temp;
        cin>>temp;
        ++bMap[temp];
    }
    teamB.pb(0);
    cntB.pb(0);
    for(auto it=bMap.begin();it!=bMap.end();++it){
        teamB.pb(it->F);
        cntB.pb(it->S+cntB.back());
    }

    ll maxDiff=LLONG_MIN;
    ll aScore,bScore;

    int foo=teamA.size(),bar=teamB.size();
    REP(i,foo){
        ll tempA=3*n-cntA[i];
        ll temp=binarySearchB(0,bar-1,teamA[i]);
        ll tempB=3*m-cntB[temp];

        if(maxDiff<tempA-tempB){
            aScore=tempA;
            bScore=tempB;
            maxDiff=tempA-tempB;
        }
        else if(maxDiff==tempA-tempB && tempA>aScore){
            aScore=tempA;
            bScore=tempB;
        }
    }

    REP(i,bar){
        ll tempB=3*m-cntB[i];
        ll temp=binarySearchA(0,foo-1,teamB[i]);
        ll tempA=3*n-cntA[temp];

        if(maxDiff<tempA-tempB){
            aScore=tempA;
            bScore=tempB;
            maxDiff=tempA-tempB;
        }
        else if(maxDiff==tempA-tempB && tempA>aScore){
            aScore=tempA;
            bScore=tempB;
        }
    }

    cout<<aScore<<":"<<bScore<<endl;

    return 0;
}
