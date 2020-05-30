#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

int main()
{
ios_base::sync_with_stdio(0);
	string s,r="";
	cin>>s;
	if(s.find('.') == -1)s.push_back('.');
	s+="00";
	bool f = s[0]=='-';
	if(f)cout<<'(';
	if(f)r.push_back(')');
	cout<<'$';
	reverse(s.begin(),s.end());
	if(f)s.pop_back();
	int i,j;
	for(i = 0; s[i+2] != '.'; ++i);
	for(j = 0; j < 4; ++j)r.push_back(s[i+j]);
	for(; i + j < s.size(); ++j)
	{
		if(j%3 == 0)r.push_back(',');
		r.push_back(s[i+j]);
	}
	reverse(r.begin(),r.end());
	cout<<r<<endl;
	return 0;
}
