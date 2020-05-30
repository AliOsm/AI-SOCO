#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define BUG cerr<<"BUG\n";

typedef long long ll;

using namespace std;

const int N=1001;
int a[N];

int main() {
    int n;
    scanf("%d",&n);
    REP(i,n)scanf("%d",a+i);
    cout<<count(a,a+n,1)<<"\n";
    a[n]=1;
    bool f=1;
    REP1(i,1,n+1){
        if(a[i]==1){
            if(f)f=0;
            else cout<<" ";
            cout<<a[i-1];
        }
    }
    cout<<"\n";
}