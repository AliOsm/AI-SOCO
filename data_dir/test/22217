#include <bits/stdc++.h>
using namespace std;
#define pii 		pair<int,int>
#define cin(n) 		scanf("%d",&n)
#define cout(n) 	printf("%d",n)
int main()
{
	pii a[300];
	int n,i,j,c=0;
	bool left,right,up,down;
	left = right = up = down = false;
	cin(n);
	for(i=1;i<=n;i++)
	{
		cin(a[i].first);
		cin(a[i].second);
	}
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
		{
			if(i==j)	continue;
			if(a[j].second == a[i].second)
			{
				if(a[j].first < a[i].first)	left = true;
				else if(a[j].first > a[i].first) right = true;
			}
			if(a[j].first == a[i].first)
			{
				if(a[j].second < a[i].second)	down = true;
				else if(a[j].second > a[i].second) up = true;
			}
		}
		if(left && right && up && down)		c++;
		left = right = up = down = false;
	}
	cout(c);
	return 0;
}
