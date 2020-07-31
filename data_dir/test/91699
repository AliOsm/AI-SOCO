#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

vector<int> T[30];
LL X[30], Y[30];

void f(int id, int p, LL x, LL y, LL dx, LL dy)
{
	X[id] = x;
	Y[id] = y;
	LL xx[3] = {dx, abs(dy), -abs(dy)};
	LL yy[3] = {dy, abs(dx), -abs(dx)};
	vector<int> ids;
	for(int i:T[id])
		if(i!=p)
			ids.push_back(i);
	for(int i = 0; i < ids.size(); ++i)
	{
		f(ids[i],id, x+xx[i], y+yy[i], xx[i]/2, yy[i]/2);
	}
}

int main()
{
    ios_base::sync_with_stdio(0);
    int n, a, b;
    cin>>n;
    for(int i = 1; i < n; ++i)
    {
    	cin>>a>>b;
    	--a,--b;
    	T[a].push_back(b);
    	T[b].push_back(a);
    }
    for(int i = 0; i < n; ++i)
    {
    	if(T[i].size()>4)return cout<<"NO", 0;
    }
    for(int i = 0; i < n; ++i)
    {
    	if(T[i].size()==1)
    	{
    		f(i,-1,-1e18,0,1e18,0);
    		break;
    	}
    }
    cout<<"YES\n";
    for(int i = 0; i < n; ++i)
		cout<<X[i]<<' '<<Y[i]<<'\n';
	return 0;
}