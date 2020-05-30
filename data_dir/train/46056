#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <string>
#include <cstring>
#include <cstdio>
// DON'T DIVIDE
// Greedy, Prefix, Sets/Bsearch, Dfs/bfs, DP
// Stack, Bitmask, Dsu 
using namespace std;

int n;
const int MAXN = 100005;
int a[MAXN];

int main()
{
	ios::sync_with_stdio(0);
	cin >> n;

	for(int i = 0; i < n; i++)
		cin >> a[i];

	int ans = 0, curr = 1;
	for(int i = 1; i < n; i++)
	{
		if(a[i] > a[i - 1])
			curr++;
		else
		{
			ans = max(ans, curr);
			curr = 1;
		}
	}

	ans = max(ans, curr);
	cout << ans << "\n";

	return 0;
}