#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for (int i = (a); i >= (b); --i)
#define L 1e5
#define pb push_back
typedef long long ll;
typedef long double ld;
std::map<int, int> counter;
int modu=1000000007;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n,a;
	cin>>n;
	std::vector<int> v[n+1];
	FOR(i,1,n)
	{
		cin>>a;
		v[a].pb(i+1);
	}
	FOR(i,1,n+1)
	{
		int temp=v[i].size();
		if(temp>0)
		{
			int ans=0;
			FOR(j,0,temp)if(v[v[i][j]].size()==0)ans++;
			if(ans<3){cout<<"No";return 0;}
		}
	}
	cout<<"Yes";
	return 0;
}