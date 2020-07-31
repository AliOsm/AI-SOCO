#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	int a,b;
	cin>>a>>b;
	while(true)
	{
		++a;
		int c = a, t = b;
		while(c && c%10 != 4 && c%10 != 7)c/=10;
		while(c && c%10 == t%10)
		{
			c/=10, t/=10;
			while(c && c%10 != 4 && c%10 != 7)c/=10;
		}
		if(c==t)return cout<<a,0;
	}
	return 0;
}
