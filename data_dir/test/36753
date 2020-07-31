#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,m; cin>>n>>m;
	vector<vector<int>> a(n,vector<int>(m));
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			cin>>a[i][j];
	vector<set<int>> row(n), col(m);
	vector<map<int,int>> orow(n), ocol(m);
	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++)
			row[i].insert(a[i][j]);
		int ord=0;
		for (auto x : row[i])
			orow[i][x]=ord++;
	}
	for (int j=0; j<m; j++) {
		for (int i=0; i<n; i++)
			col[j].insert(a[i][j]);
		int ord=0;
		for (auto x : col[j])
			ocol[j][x]=ord++;
	}

	for (int i=0; i<n; i++) {
		for (int j=0; j<m; j++) {
			int ii=orow[i][a[i][j]], jj=ocol[j][a[i][j]];
			int w=orow[i].size(), l=ocol[j].size();
			cout << max(ii,jj)+max(l-jj,w-ii) << " ";
		}
		cout << endl;
	}
	return 0;
}
