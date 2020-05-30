/*
#####################################################
# I will win.. maybe not immediately but definitely #
#####################################################
*/

#include <iostream>
#include <string>
#include <queue>
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

    string str;
    cin>>str;

    int cnt[4]={0};
    int len=str.length();
    REP(i,len)
        if(str[i]==49 || str[i]==50 || str[i]==51)
            ++cnt[str[i]-48];

    qi ans;
    while(cnt[1]--)
        ans.push(1);

    while(cnt[2]--)
        ans.push(2);

    while(cnt[3]--)
        ans.push(3);

    cout<<ans.front();
    ans.pop();

    while(!ans.E){
        cout<<"+"<<ans.front();
        ans.pop();
    }

    cout<<endl;

    return 0;
}
