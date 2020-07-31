#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define pb(x) push_back(x)
#define fi first
#define se second
#define all(x) x.begin(),x.end()
#define double long double
#define mk(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;

int n;
int a[101];

int main() {
    #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    #endif
	
    scanf("%d",&n);
    REP(i,n/2)scanf("%d",a+i);
    sort(a,a+n/2);
    int m=0;
    REP(i,n/2){
    	m+=abs(a[i]-((i+1)*2));
    }
    int m2=0;
    REP(i,n/2){
    	m2+=abs(a[i]-((i+1)*2-1));
    }
    printf("%d\n", min(m,m2));
    return 0;
}