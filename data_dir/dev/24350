#include <algorithm>
#include <iostream>
#include <iterator>
#include <iomanip>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define rfile freopen("ladder.in", "r", stdin)
#define wfile freopen("ladder.out", "w", stdout)
#define files rfile; wfile

typedef long long ll;
typedef long double ld;
typedef vector< int > vi;
typedef vector< vi > vvi;
typedef map< ll, ll > mapT;
typedef pair< int, int > pairT;

int main()
{
    int n, m;
    ll k;
    scanf("%d %d %lld", &n, &m, &k);
    ll l = 0, r = 1e12;
    while (l < r - 1)
    {
        ll mid = (l + r) / 2, t = 0;
        for (int i = 0; i < n; i++)
            t += min((mid - 1) / (i + 1), (ll)m);
        if (t < k)
            l = mid;
        else
            r = mid;
    }
    printf("%lld", l);
    return 0;
}