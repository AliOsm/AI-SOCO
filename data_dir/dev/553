#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define MAXN 100000
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define EPS 1e-7
#define PI  3.1415926535897932384626433832795028841971693993
#define DEG_to_RAD(X)   (X * PI / 180)

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};
//////////////////////

int n,h;
vii v;
int mini;
int resp[111111];

int main()
{
	ios::sync_with_stdio(0);
	cin >> n >> h;
	for(int i=0;i<n;++i)
	{
		int x;
		cin >> x;
		v.pb(mp(x,i));
	}
	sort(v.begin(),v.end());

	mini = INF;
	int pnt = 0;

	int ax1 = INF;
	int ax2 = -INF;
	
	ax1 = min(ax1,v[0].first+v[1].first);
	ax2 = v[n-1].first+v[n-2].first;
	
	pnt = -1;
	mini = ax2-ax1;

	ax1 = INF;
	ax2 = -INF;

	ax1 = min(ax1,v[1].first+v[2].first);
	ax2 = max(ax2,v[n-1].first+v[n-2].first);
	
	ax1 = min(ax1,v[0].first+v[1].first+h);
	ax2 = max(ax2,v[0].first+v[n-1].first+h);

	if(mini>ax2-ax1)
	{
		pnt = 0;
		mini = ax2-ax1;
	}

	for(int i=0;i<n;++i)
	{
		if(i<=pnt) resp[v[i].second]=1;
		else resp[v[i].second]=2;
	}

	cout << mini << endl;
	for(int i=0;i<n;++i)cout << resp[i] << " ";
	cout << endl;
	return 0;
}
