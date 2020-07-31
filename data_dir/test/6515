#include<bits/stdc++.h>
using namespace std;
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for (int i = (a); i >= (b); --i)
#define L 1e5
#define pb push_back
typedef long long ll;
typedef long double ld;
std::map<int, int> counter;
std::map<int, int> counter1;
std::map<int, int> counter2;
int modu=1000000007;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin>>n;
	std::vector<int> v(n);
	std::vector<int> a(n-1);
	std::vector<int> b(n-2);
	FOR(i,0,n)cin>>v[i];
	sort(v.begin(), v.end());
	FOR(i,0,n-1)cin>>a[i];
	sort(a.begin(), a.end());
	FOR(i,0,n-2)cin>>b[i];
	sort(b.begin(), b.end());
	FOR(i,0,n)
	{
		if(v[i]!=a[i])
		{
			cout<<v[i]<<endl;
			break;
		}
	}
	FOR(i,0,n-1)
	{
		if(a[i]!=b[i])
		{
			cout<<a[i];
			return 0;
		}
	}
	return 0;
}