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
ll power[19],dp[19];

string toString(ll x){
    string num="";
    if(!x)
        num+="0";
    else
        while(x){
            num=(char)(48+x%10)+num;
            x/=10;
        }

    return num;
}

ll toLL(string str){
    int len=str.length();

    ll ans=0;
    REP(i,len)
        ans=(ans<<1)+(ans<<3)+str[i]-48;

    return ans;
}

ll getVal(string str){
    if(str.size()==1)
        return (str[0]-47);

    ll ans=0;
    FOR(i,1,str[0]-48)
        ans+=power[str.length()-2];
    ans+=toLL(str.substr(1,str.length()-2));
    if(str[0]<=str[str.length()-1])
        ++ans;

    return ans+dp[str.length()-1];
}
//Main function
int main(){
    IOS;
    TIE;

    power[0]=dp[0]=1;
    power[1]=dp[1]=10;
    FOR(i,2,19){
        power[i]=(power[i-1]<<1)+(power[i-1]<<3);
        dp[i]=dp[i-1]+9*power[i-2];
    }

    ll l,r;
    cin>>l>>r;

    ll lVal=getVal(toString(l-1));
    ll rVal=getVal(toString(r));
    cout<<rVal-lVal<<endl;

    return 0;
}
