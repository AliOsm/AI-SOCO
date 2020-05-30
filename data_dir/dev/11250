#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	int c = 0,m = 0,n=0;
	char ch;
	string p = "AEIOUY";
	while(cin>>ch)
	{
		++n;
		if(p.find(ch)!=-1)
		{
			m = max(m,n-c);
			c = n;
		}
	}
	++n;
	m = max(m,n-c);
	cout<<m<<endl;
	return 0;
}