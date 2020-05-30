#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,m,x,y; cin>>n>>m;
	map<int, vector<ii>> lst;
	set<int> used;
	int i;
	for (i=1; i<=m; i++)
		cin>>x>>y,
		lst[x].push_back({x,i}),
		lst[y].push_back({y,i}),
		used.insert(x),
		used.insert(y);
	for (int j=1; j<=n; j++)
		if(used.find(j)==used.end())
			lst[j].push_back({j,i++});

	for (auto it : lst) {
		cout << it.second.size() << endl;
		for (auto it2 : it.second)
			cout << it2.first << " " << it2.second << endl;
	}
	return 0;
}
