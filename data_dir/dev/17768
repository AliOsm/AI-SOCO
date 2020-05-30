#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair< ll, ll > ii;
typedef vector< ll > vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

const int N = 101;

int a[N], b[N], n;
int ca[N], cb[N];

int main() {
  scanf("%d", &n);
  for(int i = 0; i < n; ++i) scanf("%d", a + i), ca[a[i]]++;
  for(int i = 0; i < n; ++i) scanf("%d", b + i), cb[b[i]]++;
  int s = 0;
  for(int i = 1; i <= 5; ++i) {
    if((ca[i] + cb[i]) % 2) {
      puts("-1");
      exit(0);
    }
    int d = (ca[i] + cb[i]) / 2;
    s += abs(d - ca[i]);
  }
  printf("%d\n", s / 2);
  return 0;
}