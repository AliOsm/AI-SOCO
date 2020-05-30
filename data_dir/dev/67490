#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

const int mx=2e5+777;

int dp[mx][3], inf=1e9, par[mx][3];

int main() {
	cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
	int n; cin>>n;
	string s; cin>>s;
	string p="RGB";
	for (int j=0; j<3; j++) {
		dp[0][j]=int(p[j]!=s[0]);
		par[0][j]=-1;
	}
	for (int i=1; i<n; i++) {
		for (int j=0; j<3; j++) {
			int cur=inf, prev=-1;
			for (int k=0; k<3; k++)
				if(k!=j) {
					int val=dp[i-1][k]+int(p[j]!=s[i]);
					if(cur>val) {
						cur=val;
						prev=k;
					}
				}
			dp[i][j]=cur;
			par[i][j]=prev;
		}
	}
	int idx=-1, val=1e9;
	for (int j=0; j<3; j++)
		if(val>dp[n-1][j])
			val=dp[n-1][j], idx=j;
	string ret; ret+=p[idx];
	for (int i=n-1; i>0; i--)
		ret+=p[par[i][idx]], idx=par[i][idx];
	reverse(ret.begin(), ret.end());
	cout << val << endl;
	cout << ret << endl;
	return 0;
}
