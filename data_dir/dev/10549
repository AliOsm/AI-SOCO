#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,m; cin>>n>>m;
	int g[n][m];
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			cin>>g[i][j];
	for (int i=n-2; i>=0; i--) {
		for (int j=m-2; j>=0; j--) {
			if(g[i][j]) continue;
			g[i][j]=min(g[i+1][j],g[i][j+1])-1;
		}
	}
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++)
			if((j<m-1&&g[i][j]>=g[i][j+1])||(i<n-1&&g[i][j]>=g[i+1][j])) {
				cout<<-1<<endl;
				return 0;
			}
	}
	ll ret=0;
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			ret+=g[i][j];
	cout<<ret<<endl;
	return 0;
}
