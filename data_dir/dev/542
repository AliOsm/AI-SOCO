#include <bits/stdc++.h>

#define forsn(i,s,n) for(tint i=(s);i<(tint)(n); i++)
#define forn(i,n) forsn(i,0,n)
#define dforn(i,n) for(tint i = tint(n)-1; i >= 0; i--)
#define debug(x) cout << #x << " = "  << x << endl

using namespace std;

typedef long long tint;

void imprimirVector (vector<tint> v)
{
	if (!v.empty())
	{ 
		tint p = tint(v.size());
		cout << "[";
		forn(i,p-1)
			cout << v[i] << ",";
		cout << v[p-1] << "]" << endl;
	}
	else
		cout << "[]" << endl;
}


int main()
{
	#ifdef ACMTUYO
		assert(freopen("entrada.in", "r", stdin));
	#endif
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	tint n,a,b;
	while (cin >> n >> a >> b)
	{
		vector<tint> x (n), vx (n), vy (n);
		map<tint, map<tint,tint> > h;
		map<tint,tint> s;
		forn(i,n)
		{
			cin >> x[i] >> vx[i] >> vy[i];
			h[a*vx[i]-vy[i]][vx[i]]++;
			s[a*vx[i]-vy[i]]++;
			
		}
		tint ans = 0;
		for (auto z : h)
			for (auto zz : z.second)
				ans += (s[z.first]-zz.second)*zz.second;
		cout << ans << "\n";
			
		
		
	}
	
	return 0;
}




