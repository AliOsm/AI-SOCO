#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define BUG cerr<<"BUG\n";

typedef long long ll;

using namespace std;

int n;
const int N=2e5+10;
int cnt[N+N];
int pref[N];
int main(){
    int k;
    scanf("%d%d",&n,&k);

    int s=0,b=0,pos=-1;
    REP(i,n){
        int x;
        scanf("%d",&x);
        if(x==k)pos=i;
        if(x<k)s++;
        else if(x>k)b++;
        if(pos!=-1)cnt[s-b+N]++;
        pref[i]=s-b;
    }

    ll ret=0,diff=N;
    REP(i,pos+1){
        ret+=cnt[diff]+cnt[diff-1];
        diff=N+pref[i];
    }
    printf("%lld\n",ret);
}