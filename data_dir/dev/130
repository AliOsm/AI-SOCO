#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair<ll,ll> ii;
typedef vector<ll> vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s)) //LASTBIT
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

//////////////////////
int dx[] = {1,-1,0,0};
int dy[] = {0,0,-1,1};
//////////////////////

const ll md = 100000000LL;

ll addMod( ll a, ll b )
{
	return (a+b)%md;
}

const int N = 110;

ll pd[N][N][11][11];
short memo[N][N][11][11];
ll n1,n2,k1,k2;

ll func( int a, int b, int qa, int qb )
{
	if( a < 0 ) return 0;
	if( b < 0 ) return 0;
	if( qa > k1 || qb > k2 ) return 0;
	if( a == 0 && b == 0 ) return 1LL;
	if( memo[a][b][qa][qb] ) return pd[a][b][qa][qb];
	memo[a][b][qa][qb] = 1;
	return pd[a][b][qa][qb] = addMod(func(a-1,b,qa+1,0),func(a,b-1,0,qb+1)); 
}

int vis[N][N];

void back( int a, int b, int op )
{
	if( vis[a][b] ) return;
	vis[a][b] = 1;
	for(int i=0;i<=k1;++i)
	{
		for(int j=0;j<=k2;++j)
		{
			if( !op )
			{
				if( a < n1 ) back(a+1,b,op^1);
				else if( b < n2 ) back(a,b+1,op^1);
			}
			else
			{
				if( b < n2 ) back(a,b+1,op^1);
				else if( a < n1 ) back(a+1,b,op^1);
			}
		}
	}
}

int main()
{
	//ios::sync_with_stdio(0);
	cin >> n1 >> n2 >> k1 >> k2;
	back(0,0,0);
	cout << func(n1,n2,0,0) << endl;
	return 0;
}