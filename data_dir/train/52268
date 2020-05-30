#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[101][500000];
int mod = 1e9+7, off = 250000;

int main()
{
	ios_base::sync_with_stdio(0);
	int a,b,k,t;
	cin>>a>>b>>k>>t;
	A[0][a-b+off] = 1;
	for(int i = 1; i <= t; ++i)
	{
		LL l = 0, r = 0, cur = 0;
		for(int j = 2*k; j < 480000; ++j)
		{
			/*if(j>off-5 && j<off+5)
			{
				cerr<<l<<' '<<r<<' '<<cur<<endl;
			}*/
			A[i][j-1] = cur;
			cur = (mod+cur-l+r)%mod;
			l = (mod+l-A[i-1][j-2*k-1]+A[i-1][j])%mod;
			r = (mod+r-A[i-1][j]+A[i-1][j+2*k+1])%mod;
		}
	}
	/*
	for(int j = off-5; j <= off+5; ++j)
	{
		for(int i = 0; i < 5; ++i)cerr<<'\t'<<A[i][j];cerr<<endl;
	}
	*/
	LL res = 0;
	for(int i = 1+off; i < 500000; ++i)res = (res+A[t][i])%mod;
	cout<<res<<endl;
	return 0;
}