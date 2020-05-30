#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int D[100001], A[100001];
int CD[100001], CA[100001];
bool F[100001];

int n,m;

bool solve(int p)
{
	memset(CD, 0, sizeof(CD));
	memset(CA, 0, sizeof(CA));
	memset(F, 0, sizeof(F));
	F[0] = true;
	stack<int>st;
	while(p)
	{
		if(!F[D[p]])
		{
			st.push(D[p]);
			F[D[p]] = true;
		}
		else
		{
			while(!st.empty() && CA[st.top()]==A[st.top()])st.pop();
			if(!st.empty())
				++CA[st.top()];
		}
		--p;
	}
	for(int i = 0; i <= m; ++i)if(CA[i] != A[i])return false;
	return true;
}

int main()
{
	cin>>n>>m;
	for(int i = 1; i <= n; ++i)cin>>D[i];
	for(int i = 1; i <= m; ++i)cin>>A[i];
	int l = 1, r = n;
	if(!solve(r))return cout<<-1<<endl,0;
	int mid;
	while(l+1<r)
	{
		mid = (l+r+1)/2;
		if(solve(mid))r = mid;
		else l = mid;
	}
	cout<<r<<endl;
	return 0;
}