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
#define qi queue<int>
#define PQ priority_queue

//general
#define E empty()

//Declare all variables and methods needed between this comment and the next one(OCD lol)
map<ll,int> cnt;

struct TrieNode{
    TrieNode *child[2]={};
};

TrieNode *root;

void trieInsert(ll x){
    ++cnt[x];

    if(cnt[x]==1){
        di d;
        REP(i,32){
            d.push_front(x%2LL);
            x/=2LL;
        }

        TrieNode *curNode=root;
        REP(i,32){
            if(!curNode->child[d[i]])
                curNode->child[d[i]]=new TrieNode();
            curNode=curNode->child[d[i]];
        }
    }
}

void trieDelete(ll x){
    --cnt[x];

    if(!cnt[x]){
        di d;
        REP(i,32){
            d.push_front(x%2LL);
            x/=2LL;
        }

        TrieNode *curNode=root;
        TrieNode *toDelete;
        int digit;

        REP(i,32){
            if(curNode->child[!d[i]]){
                toDelete=curNode;
                digit=d[i];
            }
            curNode=curNode->child[d[i]];
        }

        toDelete->child[digit]=NULL;
    }
}

ll trieQuery(ll x){
    di d;
    REP(i,32){
        d.push_front(!(x%2LL));
        x/=2LL;
    }

    TrieNode *curNode=root;
    ll ans=0LL;

    REP(i,32){
        ans=ans*2LL;
        if(curNode->child[d[i]]){
            ++ans;
            curNode=curNode->child[d[i]];
        }
        else
            curNode=curNode->child[!d[i]];
    }

    return ans;
}

//Main function
int main(){
    IOS;
    TIE;

    int q;
    cin>>q;

    root=new TrieNode();
    trieInsert(0LL);

    while(q--){
        char c;
        ll x;

        cin>>c>>x;

        if(c=='+')
            trieInsert(x);
        else if(c=='-')
            trieDelete(x);
        else
            cout<<trieQuery(x)<<endl;
    }

    return 0;
}
