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

const int N = 4444;

ll csum[N];
ll cnt[1000000];

int main()
{
	ll a;
	string s;
	cin >> a;
	cin >> s;
	int n = s.size();
	
	for(int i=0;i<n;++i)
	{
		ll at = 0;
		for(int j=i;j<n;++j)
		{
			at+=(s[j]-'0');
			cnt[at]++;
		}
	}	

	ll resp = 0;
	if( a == 0 )
	{
		resp+=cnt[0]*cnt[0];
	}

	for(int i=1;i<=9*n;++i)
	{
		if( a%i == 0 && a/i<=i )
		{
			ll sum = cnt[i]*cnt[a/i];
			if(a/i!=i) sum*=2;
			resp+=sum;
		}
	}

	cout << resp << endl;
	return 0;
}
