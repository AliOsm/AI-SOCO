#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int mod=998244353;

ll dp[1077][2][2][2077];

int B=0, W=1;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,k; cin>>n>>k;
	dp[1][B][B][1]=1;
	dp[1][B][W][2]=1;
	dp[1][W][B][2]=1;
	dp[1][W][W][1]=1;
	for (int i=2; i<=n; i++) {
		for (int x=0; x<2; x++) for (int y=0; y<2; y++) {
			for (int u=0; u<2; u++) for (int v=0; v<2; v++) {
				int inc=0;
				if(x!=u&&y!=v) {
					if(x!=y) inc=2;
					else inc=1;
				}
				else if(x!=u) {
					if(x!=y) inc=1;
				} else if(y!=v) {
					if(x!=y) inc=1;
				}
				for (int j=0; j<=2*n; j++)
					dp[i][x][y][j+inc]=(dp[i][x][y][j+inc]+dp[i-1][u][v][j])%mod;
			}
		}
	}
	ll ret=0;
	for (int i=0; i<2; i++)
		for (int j=0; j<2; j++)
			ret=(ret+dp[n][i][j][k])%mod;
	cout << ret << endl;
	return 0;
}
