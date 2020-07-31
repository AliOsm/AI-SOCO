#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,m,steps=0,c=0;
	cin >> n >> m;
	if(n<m)
	{
		cout << -1 << endl;
		return 0;
	}
	while(steps<n)
	{
		if(n-steps == 1)
		{
			steps++;
			c++;
			continue;
		}
		steps += 2;
		c++;
	}
	if(c%m==0)
		cout << c << endl;
	else
	{
		while(c%m != 0)
		{
			c++;
		}
		cout << c << endl;
	}
		
}
