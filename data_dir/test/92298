#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

pii A[1001];
bool F[1001];
int par[1001];
int temp[1001];
vector<pii> V[1001];
int dp[1001][1001];

int root(int v){return par[v] < 0 ? v : (par[v] = root(par[v]));}
void merge(int x,int y){
        if((x = root(x)) == (y = root(y)))     return ;
	if(par[y] < par[x])
		swap(x, y);
	par[x] += par[y];
	par[y] = x;
}


int main()
{
	int n,m,w,a,b;
	cin>>n>>m>>w;
	memset(par,-1,sizeof(par));
	for(int i = 1; i <= n; ++i)cin>>A[i].first;
	for(int i = 1; i <= n; ++i)cin>>A[i].second;
	while(m--)
	{
		cin>>a>>b;
		merge(a,b);
	}
	int til = 0;
	for(int i = 1; i <= n; ++i)
	{
		if(F[root(i)])V[temp[root(i)]].push_back(A[i]);
		else
		{
			temp[root(i)] = ++til;
			V[temp[root(i)]].push_back(A[i]);
			F[root(i)] = true;
		}
	}
	
	for(int i = 1; i <= til; ++i)
	{
		int sumb = 0, sumw = 0;
		for(auto it:V[i])sumw += it.first, sumb += it.second;
		for(int j = 0; j <= w; ++j)dp[i][j] = dp[i-1][j];
		for(int j = sumw; j <= w; ++j)
		{
			if(j>0)dp[i][j] = max(dp[i][j-1],dp[i][j]);
			dp[i][j] = max(dp[i-1][j-sumw]+sumb,dp[i][j]);
		}
		for(auto it:V[i])
		{
			for(int j = it.first; j <= w; ++j)
			{
				if(j>0)dp[i][j] = max(dp[i][j-1],dp[i][j]);
				dp[i][j] = max(dp[i-1][j-it.first]+it.second,dp[i][j]);
			}
		}
		for(int j = 1; j <= w; ++j)
		{
			dp[i][j] = max(dp[i][j-1],dp[i][j]);
		}
	}
	int res = 0;
	for(int i = 0; i <= w; ++i)res = max(res,dp[til][i]);
	cout<<res<<endl;
	return 0;
}