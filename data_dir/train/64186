#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

bool A[200001];
int T[200001],D[200001];

int main()
{
	ios_base::sync_with_stdio(0);
	int n, t, k, a;
	cin>>n>>t>>k;
	int p = 1, cur = 2;
	for(int i = 1; i<=t; ++i)
	{
		cin>>a;
		for(int j = 0; j < a; ++j)
		{
			D[cur] = i;
			T[cur++] = p;
			A[p] = true;
		}
		while(D[p] < i)++p;
	}
	for(int i = 2; i <= n; ++i)if(!A[i])--k;
	p = 1;
	for(int i = 2; i <= n; ++i)
	{
		if(D[i]!=D[i-1])continue;
		while(p<n && D[p]<D[i]-1)++p;
		while(p<n && A[p])++p;
		if(!A[p] && D[p] == D[i]-1)
		{
			if(k<0)
			{
				++k;
				A[p] = true;
				T[i] = p;
			}
		}
	}
	if(k)return cout<<"-1\n",0;
	cout<<n<<'\n';
	for(int i = 2; i <= n; ++i)cout<<T[i]<<' '<<i<<'\n';
	return 0;
}