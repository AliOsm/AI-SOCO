#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

pii cars[200000];
int A[200002];
int n,k,s,t;

bool f(int c)
{
	int res = 0;
	for(int i = 0; i <= k; ++i)
	{
		if(A[i]>c)return false;
		res += 2*A[i] - min(c-A[i],A[i]);
	}	
	return res <= t;
}

int main()
{
ios_base::sync_with_stdio(0);
	cin>>n>>k>>s>>t;
	for(int i = 0; i < n; ++i)cin>>cars[i].first>>cars[i].second;
	for(int i = 1; i <= k; ++i)cin>>A[i];
	sort(A+1,A+k+1);
	A[k+1] = s;
	for(int i = 0; i <= k; ++i)A[i] = A[i+1]-A[i];
	int l = 0, r = 1e9+1, m;
	while(l<r)
	{
		m = (l+r)/2;
		if(f(m))r = m;
		else l = m+1;
	}
	int p = 1e9+1;
	for(int i = 0; i < n; ++i)
		if(cars[i].second>=r)p = min(p,cars[i].first);
	cout<<(p==1e9+1?-1:p)<<endl;
	return 0;
}