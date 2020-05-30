#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int n;
const int mx=5277;
bool grid[mx][mx];

bool ok(int d) {
	for (int i=0; i<n; i+=d)
		for (int j=0; j<n; j+=d)
			for (int x=0; x<d; x++)
				for (int y=0; y<d; y++)
					if(grid[i+x][j+y]!=grid[i][j])
						return false;
	return true;
}

int main() {
	scanf("%d", &n);
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j+=4) {
			int scan;
			scanf("%1x", &scan);
			bitset<4> bits=bitset<4>(scan);
			for (int w=3, v=0; w>=0; w--, v++)
				grid[i][j+v]=bits[w];
		}
	}
	set<int> div;
	for (int d=1; d*d<=n; d++)
		if(n%d==0)
			div.insert(d), div.insert(n/d);
	int ret=0;
	for (auto it=div.rbegin(); it!=div.rend(); it++)
		if(ok(*it)) {
			ret=*it;
			printf("%d\n", ret);
			break;
		}
	return 0;
}
