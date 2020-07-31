#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define fi first
#define se second

typedef long long ll;

using namespace std;



int n,m;
const int N=101,M=1001;
int a[M];
double E[N][M*N+1];

int main() {
     #ifndef ONLINE_JUDGE
    freopen("in.txt","r",stdin);
    #endif

    scanf("%d%d",&n,&m);
    if(m==1){
    	printf("1\n");
    	return 0;
    }
    int me=0;
    REP(i,n)scanf("%d",&a[i]),me+=a[i];
    REP1(i,1,m+1)if(i!=a[0])E[0][i]=1;
    REP1(i,1,n){
    	REP1(j,1,M*N+1)
    		E[i-1][j]+=E[i-1][j-1];
    	REP1(j,1,M*N+1){
    		E[i][j]=j-a[i]-1>=0?max(0.0,E[i-1][j-a[i]-1]-E[i-1][max(0,j-m-1)]):0;
    		E[i][j]+=max(0.0,E[i-1][j-1]-E[i-1][max(0,j-a[i])]);
    		E[i][j]/=m-1;
    	}
    }

    double r=0;
    REP1(i,1,me)r+=E[n-1][i];
    printf("%.11f\n", r+1.0);
    return 0;
}