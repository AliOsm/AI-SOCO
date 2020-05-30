#include <bits/stdc++.h>
using namespace std;

int main() {
	bool vis[31234];
	int x,n;
	memset(vis,false,sizeof(vis));
	cin >> n;
	for(int i=1; i<=n; ++i) {
		cin >> x;
		vis[x] = true;
	}
	int i=0;
	while(++i) {
		if(!vis[i]) {
			cout << i << endl;
			return 0;
		}
	}
}