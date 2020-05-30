#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cstring>
// DON'T DIVIDE
// Greedy, Prefix, Sets/Bsearch, Dfs/bfs, DP
// Stack, Bitmask, Dsu 
using namespace std;

int n, k;

int main()
{
	ios::sync_with_stdio(0);
	cin >> n >> k;

	int curr = 240 - k;
	int ans = 0;
	for(int i = 1; i <= n; i++)
		if(curr >= 5 * i)
		{
			ans++;
			curr -= 5 * i;
		}

	cout << ans << "\n";
	return 0;
}