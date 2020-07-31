#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n)	for(i=0;i<n;i++)
typedef long long ll;
ll loc,x=0,y=0,c=0;
ll h[1234567],m[1234567];
int main()
{
	string s;
	cin >> s;
	ll i=0;
	FOR(i,s.length())
	{
		if(s[i]=='h')
		{
			loc = i;
			if(s[i+1]=='e')
			{
				i++;
				if(s[i+1]=='a')
				{
					i++;
					if(s[i+1]=='v')
					{
						i++;
						if(s[i+1]=='y')
						{
							i++;
							h[x++] = loc;
						}
					}
				}
			}
		}
		else if(s[i]=='m')
		{
			loc = i;
			if(s[i+1]=='e')
			{
				i++;
				if(s[i+1]=='t')
				{
					i++;
					if(s[i+1]=='a')
					{
						i++;
						if(s[i+1]=='l')
						{
							i++;
							m[y++] = loc;
						}
					}
				}
			}
		}
	}
	for(i=0;i<y;i++)
		c += (ll)(lower_bound(h,h+x,m[i])-h);
	cout << c << endl;
	return  0;
}













//?
