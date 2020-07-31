#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <list>
#include <bitset>

using namespace std;

#define fi first
#define se second
#define long long long
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
ii operator+ (ii a, ii b) { return {a.fi+b.fi,a.se+b.se}; }

bool ada[31];

int main()
{
	//ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	// freopen("input.in", "r", stdin);

	int n, k;
	scanf("%d %d", &n, &k);

	bool bol = 0;
	for(int i = 1; i <= n; i++)
	{
		int bit = 0;
		for(int j = k-1; j >= 0; j--)
		{
			int x; scanf("%d", &x);
			bit += x*(1<<j);
		}
		// printf("%d\n", bit);
		if(bit == 0) bol = 1;
		for(int j = 0; j < (1<<k); j++)
		{
			// printf("	%d\n", j);
			if((bit&j) == 0 && ada[j])
				bol = 1;
		}
		ada[bit] = 1;
	}
	if(bol) printf("Yes\n");
	else printf("No\n");
}










