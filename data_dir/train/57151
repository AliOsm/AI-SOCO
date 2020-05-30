#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int A[256];

int main()
{
ios_base::sync_with_stdio(0);
	int n;
	char c;
	cin>>n;
	while(n--)
	{
		cin>>c;
		++A[c];
	}
	set<char> res;
	if(A['R']&&A['G']&&A['B'])res.insert('R'),res.insert('G'),res.insert('B');
	if(bool(A['R']) + bool(A['G']) + bool(A['B']) == 2)
	{
		if(!A['R'])
		{
			res.insert('R');
			if(A['G']>1)res.insert('B');
			if(A['B']>1)res.insert('G');
		}
		if(!A['G'])
		{
			res.insert('G');
			if(A['R']>1)res.insert('B');
			if(A['B']>1)res.insert('R');
		}
		if(!A['B'])
		{
			res.insert('B');
			if(A['G']>1)res.insert('R');
			if(A['R']>1)res.insert('G');
		}
	}
	if(bool(A['R']) + bool(A['G']) + bool(A['B']) == 1)
	{
		if(A['R'])res.insert('R');
		if(A['G'])res.insert('G');
		if(A['B'])res.insert('B');
	}
	for(auto i:res)cout<<i;cout<<endl;
	return 0;
}
