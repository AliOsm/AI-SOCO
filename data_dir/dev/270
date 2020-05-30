#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ll long long
#define maxn 300005
#define fr(i,j,k) for(int i=j;i<k;i++)
#define f(n) fr(i,0,n)
#define f1(n) fr(i,1,n+1)
#define ms(i) memset(i,0,sizeof(i));
#define ms1(i) memset(i,-1,sizeof(i));
#define F first
#define S second
const int mod = 1e9 + 7;
vector<int>cdl[5005];
int nd[5005], g[5005], pt[5005];
int dl[5005];
bool cmp(int x,int y){
    return pt[x] > pt[y];
}
int dp[5005][5005];
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n, m, k;
    cin >> n >> m >> k;
        f1(n){
        dl[i] = i;
    }
    f1(n){
        cin >> nd[i] >> g[i] >> pt[i];
    }
    f(m){
        int add1, add2;
        cin >> add1 >> add2;
        dl[add2] = max(dl[add2],add1);
    }
    f1(n){
        cdl[dl[i]].pb(i);
    }
    int cur = k;
    int c[n+5];
    for(int i = 1 ; i <= n ; i++){
        c[i] = cur;
        if(cur < nd[i]){
            cout << -1 << endl;
            exit(0);
        }
        cur += g[i];
    }
    int coda[n+5];
    int mi = cur;
    for(int i = n ; i >= 1 ; i--){
        coda[i] = mi;
        mi = min(mi,c[i]-nd[i]);
    }
    f1(n){
        sort(cdl[i].begin(),cdl[i].end(),cmp);
    }
    int mx = 0;
    for(int i = 1 ; i <= n ;i++){
        vector<int>pre;
        pre.pb(0);
        for(int j = 0 ; j < cdl[i].size() ; j++){
            pre.pb(pre.back()+pt[cdl[i][j]]);
        }
        for(int j = 0 ; j <= coda[i] ; j++){
            for(int k = 0 ; k < pre.size() ; k++){
                if(k > j)break;
                dp[i][j] = max(dp[i][j],dp[i-1][j-k]+pre[k]);
            }
            mx = max(mx,dp[i][j]);
        }
    }
    cout << mx << endl;
}
