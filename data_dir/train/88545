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

//Main function
int main(){
    IOS;
    TIE;

    int n;
    cin>>n;

    int arr[n],sorted[n];
    REP(i,n){
        cin>>arr[i];
        sorted[i]=arr[i];
    }

    sort(sorted,sorted+n);

    bool flag=true;
    REP(i,n)
        if(arr[i]!=sorted[i]){
            flag=false;
            break;
        }

    if(flag){
        cout<<"yes"<<endl;
        cout<<"1 1"<<endl;
        return 0;
    }

    flag=true;
    DFOR(i,n-1,0)
        if(arr[i]!=sorted[n-1-i]){
            flag=false;
            break;
        }

    if(flag){
        cout<<"yes"<<endl;
        cout<<"1 "<<n<<endl;
        return 0;
    }
    else{
        int leftPtr=0;
        while(arr[leftPtr]==sorted[leftPtr])
            ++leftPtr;

        int rightPtr=n-1;
        while(arr[rightPtr]==sorted[rightPtr])
            --rightPtr;

        flag=true;
        DFOR(i,rightPtr-1,leftPtr)
            if(arr[i]<arr[i+1]){
                flag=false;
                break;
            }

        if(flag)
            cout<<"yes"<<endl<<leftPtr+1<<" "<<rightPtr+1<<endl;
        else
            cout<<"no"<<endl;
    }

    return 0;
}
