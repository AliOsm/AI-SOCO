#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	string s;
	cin>>s;
	int f;
	for(f = 0; f < s.size(); ++f)
	{
		if(s[f] != '4' && s[f] !='7')break;
	}
	if(f<s.size())
	{
		for(int i = f+1; i < s.size(); ++i)s[i] = '4';
		if(s[f] < '4')s[f] = '4';
		else if(s[f] < '7')s[f] = '7';
		else
		{
			s[f] = '4';
			for(--f; f >= 0; --f)
			{
				if(s[f] == '4')
				{
					s[f] = '7';
					break;
				}
				else s[f] = '4';
			}
			if(f<0)
			{
				s +='4';
				for(auto &i:s)i='4';
			}
		}
	}
	if(s.size()&1)
	{
		s += '4';
		for(auto &i:s)i = '4';
	}
	int _4=0,_7=0;
	for(auto i:s)
	{
		if(i=='4')++_4;
		else ++_7;
	}
Again:
	if(_7<_4)
	{
		for(int i = s.size()-1; _7 != _4; --i)
		{
			if(s[i] == '4')
			{
				--_4;
				++_7;
				s[i] = '7';
			}
		}
	}
	if(_4<_7)
	{
		for(int i = s.size()-1; i >= 0; --i)
		{
			if(s[i] == '4')
			{
				--_4;
				++_7;
				s[i] = '7';
				if(_4>=_7)goto Again;
				s[i] = '4';
				++_4;
				--_7;
			}
			else
			{
				--_7;
				++_4;
				s[i] = '4';
			}
			
		}
		for(int j = 0; j < s.size()/2; ++j)cout<<'4';
		cout<<"47";
		for(int j = 0; j < s.size()/2; ++j)cout<<'7';
		return 0;
	}
	cout<<s;
	return 0;
}
