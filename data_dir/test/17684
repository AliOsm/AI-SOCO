#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;



int main()
{
	ios_base::sync_with_stdio(0);
	int n,t,cur=0;
	string st;
	cin>>n;
	while(n--)
	{
		cin>>t>>st;
		if((cur==0&&st[0]!='S')||(cur==20000 && st[0]!='N'))
		{
			cur = -1;
			break;
		}
		if(st[0] == 'S')cur += t;
		else if(st[0] == 'N')cur -= t;
		if(cur<0 || cur>20000)break;
	}
	cout<<(cur==0?"YES":"NO")<<endl;
	return 0;
}