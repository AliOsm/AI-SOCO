#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

LL A[100000];

int main()
{
ios_base::sync_with_stdio(0);
	int n,a,b;
	cin>>n>>a>>b;
	for(int i = 0; i < n; ++i)cin>>A[i];
	sort(A,A+n);
	if(a>b)swap(a,b);
	int t = a;
	ldb s = 0, res = 0;
	while(t--)s+=A[--n];
	if(a)res += s/ldb(a);
	s = 0;
	t = b;
	while(t--)s+=A[--n];
	if(b)res += s/ldb(b);
	cout<<setprecision(20)<<res<<endl;
}