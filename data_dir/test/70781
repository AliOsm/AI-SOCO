#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A['z'+1], B['z'+1], C['z'+1];

int main()
{
ios_base::sync_with_stdio(0);
	string a,b,c;
	cin>>a>>b>>c;
	for(auto i:a)++A[i];
	for(auto i:b)++B[i];
	for(auto i:c)++C[i];
	int bn=0,cn=0;
	for(int i = 0; i <= 1e5; ++i)
	{
		int secn = 1e5;
		for(char it = 'a'; it <= 'z'; ++it)
		{
			if(B[it]*i > A[it])
			{
				secn = -1;
				break;
			}
			secn = min(secn,C[it]?(A[it]-B[it]*i)/C[it]:int(1e5));
		}
		if(secn<0)break;
		if(i+secn > bn+cn)bn = i, cn = secn;
	}
	for(int i = 0; i < bn; ++i)cout<<b;
	for(int i = 0; i < cn; ++i)cout<<c;
	for(char i = 'a'; i <= 'z'; ++i)
	{
		for(int j = A[i] -bn*B[i] -cn*C[i]; j; --j)cout<<i;
	}
	cout<<endl;
	return 0;
}
