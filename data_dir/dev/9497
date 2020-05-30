#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll n,m,a,b,c,d;
bool bset,cset;
ll min(void);
ll max(void);
ll combinations(ll x,ll y);
int main()
{
	cin >> n >> m;
	cout << min() << " " << max() << endl;
	return 0;
}
ll max(void)
{
	ll x,y;
	x = n-m+1;
	y=2;
	return combinations(x,y);
}
ll combinations(ll x,ll y)
{
	return ((x*(x-1))/y);
}
ll min(void)
{
	return (combinations(n/m+1,2)*(n%m)+combinations(n/m,2)*(m-(n%m)));
}
