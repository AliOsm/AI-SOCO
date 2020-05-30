#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define BUG cerr<<"BUG\n";

typedef long long ll;

using namespace std;


int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    int n,d;
    cin>>n>>d;
    int cnt=2;
    vector<int>x(n);
    REP(i,n){
        cin>>x[i];
    }
    REP(i,n-1){
        if(x[i]+d<x[i+1]&&x[i+1]-(x[i]+d)>=d){
            if(x[i]+d==x[i+1]-d)cnt++;
            else cnt+=2;
        }
    }

    cout<<cnt<<"\n";

    return 0;
}