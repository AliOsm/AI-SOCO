#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,i,j,k,c;
	cin >> n;
	c = 2*n;
	for(i=0;i<=n;i++)
	{
		j=0;
		while(j<c)
		{
			printf(" ");
			j++;
		}
		for(k=0;k<=i;k++,j++)
		{
			if(i==0)	printf("%d",k);
			else	printf("%d ",k);
		}
		for(k=i-1;k>=0;k--)
		{
			if(k==0)	printf("0");
			else
				printf("%d ",k);
		}
		cout << endl;
		c -= 2;
	}
	c = 2;
	for(i=n-1;i>=0;i--)
	{
		j=0;
		while(j<c)
		{
			printf(" ");
			j++;
		}
		for(k=0;k<=i;k++)
		{
			if(i==0)	printf("%d",k);
			else	printf("%d ",k);
		}
		for(k=i-1;k>=0;k--)
		{
			if(k==0)	printf("0");
			else 	printf("%d ",k);
		}
		cout << endl;
		c += 2;
	}
}
