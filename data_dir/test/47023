#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	int n,mi=101,o=0,s=0,inp;
	cin>>n;
	while(n--)
	{
		cin>>inp;
		if(inp&1)++o,mi = min(mi,inp);
		s+=inp;
	}
	cout<<bool(o)*(s-!(o&1)*mi)<<endl;
	return 0;
}
