#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

string S[int(2e5+1)];
set<string> ss;

int main()
{
ios_base::sync_with_stdio(0);
	int n;
	cin>>n;
	while(n--)cin>>S[n];
	for(int i = 0; S[i] != ""; ++i)
	{
		if(ss.find(S[i]) == ss.end())
		{
			cout<<S[i]<<'\n';
			ss.insert(S[i]);
		}
	}
	return 0;
}
