#include <cstdio>

bool used[1001][1001][3];
double dp[1001][1001][3];

double solve(int w,int b, int ph)
{
	if(w<0||b<0) return 0;
	if(w+b==0) return 0;
	if(!used[w][b][ph])
	{
		used[w][b][ph]=1;
		if(ph==2)
		{
			dp[w][b][ph]=double(w)/(w+b)*solve(w-1,b,0)+double(b)/(w+b)*solve(w,b-1,0);
		}
		else
		{
			dp[w][b][ph]=double(w)/(w+b)*(ph==0)+double(b)/(w+b)*solve(w,b-1,ph+1);
		}
	}
	return dp[w][b][ph];
}

int main()
{
	int w,b;
	scanf("%d%d",&w,&b);
	printf("%.9lf\n",solve(w,b,0));
	return 0;
}
