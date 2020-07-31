#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for (int i = (a); i >= (b); --i)
#define L 1e5
#define pb push_back
typedef long long ll;
typedef long double ld;
std::map<ld, int> counter;
int modu=1000000007;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	ld n,x0,y0,ans=0,flag=0;
	cin>>n>>x0>>y0;
	std::vector<ld> x(n);
	std::vector<ld> y(n);
	int co=n;
	FOR(i,0,n)
	{
		cin>>x[i]>>y[i];
		if(x[i]!=x0)
			counter[(y[i]-y0)/(x[i]-x0)]++;
		else 
			flag=1;
	}
	cout<<counter.size()+flag;
	return 0;
}