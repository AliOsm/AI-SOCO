#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[int(1e5)];

int main()
{
ios_base::sync_with_stdio(0);
	int n;
	cin>>n;
	for(int i = 0; i < n; ++i)
	{
		cin>>A[i];
	}
	sort(A,A+n);
	A[0] = 1;
	for(int i = 1; i < n; ++i)
	{
		if(A[i]>A[i-1])A[i] = A[i-1]+1;
	}
	cout<<A[n-1]+1<<endl;
	return 0;
}
