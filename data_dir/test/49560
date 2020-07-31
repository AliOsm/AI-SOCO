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

int n, m;
int D[1000003], A[100003];
int tdate[100003];
long pref[100003];

bool cek(int e)
{
	// printf("E %d\n", e);
	memset(tdate, 0, sizeof tdate);
	memset(pref, 0, sizeof pref);
	for(int i = e; i >= 1; i--)
	{
		if(tdate[D[i]] == 0 && D[i])
		{
			pref[i] += 1LL*A[D[i]]+1;
			tdate[D[i]] = i;
		}
	}
	for(int i = 1; i <= m; i++)
	{
		if(tdate[i] == 0)
			return 0;
	}
	// for(int i = 1; i <= e; i++) printf("%lld ", pref[i]); printf("\n");
	for(int i = 1; i <= e; i++)
	{
		pref[i] += pref[i-1];
		if(pref[i] > i)
			return 0;
	}
	return 1;
}


int main()
{
	//ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	// freopen("input.in", "r", stdin);

	scanf("%d %d", &n, &m);
	for(int i = 1; i <= n; i++) scanf("%d", &D[i]);
	for(int i = 1; i <= m; i++) scanf("%d", &A[i]);

	int kir = 1, kan = n;
	while(kir < kan)
	{
		int mid = (kir+kan)/2;
		if(!cek(mid)) kir = mid+1;
		else kan = mid;
	}
	if(!cek(kir)) printf("-1\n");
	else printf("%d\n", kir);
}










