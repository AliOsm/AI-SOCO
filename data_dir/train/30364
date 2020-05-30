#include <bits/stdc++.h>
#include <bitset>

#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REP1(i,j,n) for(int i=j;i<(int)n;i++)
#define all(x) x.begin(),x.end()
#define double long double
#define mp(x,y) make_pair(x,y)

typedef long long ll;

using namespace std;

int n,m,d;
string s1,s2;
int MOD=1e9+7;
const int N=2001;
int mem[2][2][N][N];
int hun[N];

int dp(int dec,int inc,int idx,int mod){
    if(idx==n)return !mod;
    int &ret=mem[dec][inc][idx][mod];
    if(ret!=-1)return ret;
    ret=0;
    int l=idx&1?d:0;
    int r=idx&1?d:9;
    REP1(dig,max(l,inc?0:s1[idx]-'0'),min(r,(dec?9:s2[idx]-'0'))+1){
        if((idx&1)^(dig!=d)){
            ret+=dp(dec||dig<s2[idx]-'0',inc||dig>s1[idx]-'0',idx+1,(mod+hun[n-idx-1]*dig)%m);
            if(ret>=MOD)ret-=MOD;
        }
    }
    return ret;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    hun[0]=1;
    cin>>m>>d>>s1>>s2;
    REP1(i,1,N)hun[i]=hun[i-1]*10%m;
    n=(int)s1.length();
    memset(mem,-1,sizeof mem);
    cout<<dp(0,0,0,0)<<"\n";
}