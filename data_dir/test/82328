#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;

const int MAX=20;
ll comb[MAX][MAX];
int cnt[10];
ll mem[10][20];
ll nCr(int n,int k){
    if(n<k)return 0;
    if(k==0||k==n)return 1;
    if(comb[n][k]!=-1)return comb[n][k];
    if(n-k<k)return comb[n][k]=nCr(n,n-k);
    return comb[n][k]=nCr(n-1,k-1)+nCr(n-1,k);
}

ll dp(int dig,int mad){
    if(dig==10)return 1;
    ll &ret=mem[dig][mad];
    if(ret!=-1)return ret;
    ret=0;
    if(!cnt[dig])ret=dp(dig+1,mad);
    REP1(tak,1,cnt[dig]+1)ret+=nCr(dig==9?tak+mad-1:tak+mad,tak)*dp(dig+1,mad+tak);
    return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s;cin>>s;
    REP(i,s.length())cnt[s[i]-'0']++;
    reverse(cnt,cnt+10);
    memset(mem,-1,sizeof mem);
    memset(comb,-1,sizeof comb);
    cout<<dp(0,0)<<"\n";
}