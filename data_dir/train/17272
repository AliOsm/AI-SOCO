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
int arr[200010],tree[800010],lazy[800010];
vi pos[200010];

int qLow,qHigh,val;
void update(int low,int high,int pos){
    int mid=(low+high)>>1;

    if(lazy[pos]){
        tree[pos]=lazy[pos];
        if(low!=high)
            lazy[2*pos+1]=lazy[2*pos+2]=lazy[pos];
        lazy[pos]=0;
    }

    if(qLow>high || qHigh<low)
        return ;
    else if(qLow<=low && qHigh>=high){
        tree[pos]=val;
        if(low!=high)
            lazy[2*pos+1]=lazy[2*pos+2]=val;
    }
    else{
        update(low,mid,2*pos+1);
        update(mid+1,high,2*pos+2);
        tree[pos]=(tree[2*pos+1]>tree[2*pos+2])?tree[2*pos+1]:tree[2*pos+2];
    }
}

int query(int low,int high,int pos){
    int mid=(low+high)>>1;

    if(lazy[pos]){
        tree[pos]=lazy[pos];
        if(low!=high)
            lazy[2*pos+1]=lazy[2*pos+2]=lazy[pos];
        lazy[pos]=0;
    }

    if(qLow>high || qHigh<low)
        return 0;
    else if(qLow<=low && qHigh>=high)
        return tree[pos];
    else
        return max(query(low,mid,2*pos+1),query(mid+1,high,2*pos+2));
}
//Main function
int main(){
    IOS;
    TIE;

    int n,q;
    cin>>n>>q;

    int zeroCnt=0;
    REP(i,n){
        cin>>arr[i];
        if(!arr[i])
            ++zeroCnt;
        pos[arr[i]].pb(i);
    }

    if(zeroCnt==n){
        cout<<"YES"<<endl;
        REP(i,n)
            cout<<q<<" ";
        cout<<endl;
    }
    else if(pos[q].E && !zeroCnt)
        cout<<"NO"<<endl;
    else{
        qLow=0,qHigh=n-1,val=1;
        update(0,n-1,0);

        FOR(i,2,q+1)
            if(!pos[i].E){
                qLow=pos[i][0],qHigh=pos[i].back(),val=i;
                update(0,n-1,0);
            }

        if(pos[q].E){
            if(pos[0].E){
                cout<<"NO"<<endl;
                return 0;
            }
            else{
                qLow=pos[0][0],qHigh=pos[0][0],val=q;
                update(0,n-1,0);
            }
        }

        REP(i,n){
            qLow=i,qHigh=i;
            int temp=query(0,n-1,0);
            if(!arr[i])
                arr[i]=temp;
            else if(temp!=arr[i]){
                cout<<"NO"<<endl;
                return 0;
            }
        }

        cout<<"YES"<<endl;
        REP(i,n)
            cout<<arr[i]<<" ";
        cout<<endl;
    }

    return 0;
}
