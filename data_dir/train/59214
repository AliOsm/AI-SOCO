#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n,k; cin>>n;
	vector<int> l(n), r(n);
	for (int i=0; i<n; i++)
		cin>>l[i]>>r[i];
	cin>>k;
	int ret=n;
	for (int i=0; i<n; i++)
		ret-=int(r[i]<k);
	cout << ret << endl;
	return 0;
}
