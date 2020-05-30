#include<bits/stdc++.h>
using namespace std;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,m; cin>>n>>m;
	vector<int> a(n);
	vector<int> b(m);
	int x=0, y=0;
	for (int i=0; i<n; i++)
		cin>>a[i], x^=a[i];
	for (int i=0; i<m; i++)
		cin>>b[i], y^=b[i];
	if(x!=y) {
		cout<<"NO\n";
		return 0;
	}
	vector<vector<int>> g(n, vector<int>(m,0));
	int p=b.back(), q=a.back();
	for (int i=0; i<n-1; i++)
		g[i][m-1]=a[i], p^=a[i];
	for (int j=0; j<m-1; j++)
		g[n-1][j]=b[j], q^=b[j];
	if(p!=q) {
		cout<<"NO\n";
		return 0;
	}
	cout<<"YES\n";
	g[n-1][m-1]=p;
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			cout<<g[i][j]<<" ";
		}
		cout<<"\n";
	}
	return 0;
}
