#include<bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef tree<ii,null_type,less<ii>,rb_tree_tag,tree_order_statistics_node_update> indexed_set;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int t; cin>>t;
	while(t--) {
		int n; cin>>n;
		map<int,int> ct;
		for (int i=0; i<n; i++) {
			int x,cur=0; cin>>x;
			while(x%2==0)
				x/=2, cur++;
			ct[x]=max(ct[x],cur);
		}
		int ret=0;
		for (auto it : ct)
			ret+=it.second;
		cout<<ret<<"\n";
	}
	return 0;
}
