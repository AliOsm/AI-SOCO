#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	int a,b=0,c;
	cin>>a>>c;
	int t = 1;
	while(a|c)
	{
		b+= t*((3+c%3-a%3)%3);
		t*=3;
		a/=3;
		c/=3;
	}
	cout<<b<<endl;
	return 0;
}
