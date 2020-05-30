#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<LL,LL> pii;

int A[1000][1000];

int main()
{
ios_base::sync_with_stdio(0);
	int n,m;
	cin>>n>>m;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			cin>>A[i][j];
	int c, sum = 0, f;
	for(int i = 0; i < n; ++i)
	{
		f = 0, c = 0;
		for(int j = 0; j < m; ++j)
		{
			if(A[i][j] == 0)++c;
			else
			{
				sum+=c+c*f;
				f = 1;
				c = 0;
			}
		}
		sum += c*f;
	}
	for(int i = 0; i < m; ++i)
	{
		f = 0, c = 0;
		for(int j = 0; j < n; ++j)
		{
			if(A[j][i] == 0)++c;
			else
			{
				sum+=c+c*f;
				f = 1;
				c = 0;
			}
		}
		sum += c*f;
	}
	cout<<sum<<endl;
	return 0;
}