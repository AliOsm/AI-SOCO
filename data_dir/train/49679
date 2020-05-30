#include <bits/stdc++.h>
using namespace std;
int main()
{
	char s[200];
	int l,c=0,i,j,k;
	bool q1,q2,a;
	q1 = q2 = a = false;
	scanf("%s",s);
	l = strlen(s);
	for(i=0;i<l;i++)
	{
		if(s[i]=='Q')	q1=true;
		else 			continue;
		
		for(j=i+1;j<l;j++)
		{
			if(s[j]=='A')	a = true;
			else 	continue;
			
			for(k=j+1;k<l;k++)
			{
				if(s[k]=='Q')	c++;
			}
			
			q2 = false;
		}
		a = false;
	}
	cout << c << endl;
	return 0;
}
