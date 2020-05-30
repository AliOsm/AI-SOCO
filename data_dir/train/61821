#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

typedef long long int64;
typedef double real;

#ifdef DEBUG
#define eprintf(...) fprintf (stderr, __VA_ARGS__)
#else
#define eprintf(...) assert (true)
#endif

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

using namespace std;

const int MedN = 100, MaxN = MedN << 1, MaxL = 120;
const int NA = -1, MaxC = 0x3F3F3F3F;

real a [MaxN + 1];
real f [2] [MaxN + 1];
int n;

int main (void)
{
 int b, i, j, k, v;

 while (scanf (" %d", &n) != EOF)
 {
  for (i = 0; i <= n; i++)
   scanf (" %lf", &a[i]);

  b = 0;
  for (i = 0; i <= MaxN; i++)
   f[b][i] = -MaxC;
  for (i = 0; i <= n; i++)
   for (j = 0; j <= n; j++)
   {
    v = i + j - n;
    v += MedN;
    f[b][v] = max (f[b][v], (a[i] + a[j]) * 0.5);
   }

  for (k = 0; k < MaxL; k++)
  {
/*
   for (i = MedN - 3; i <= MedN + 3; i++)
    printf ("%.6lg%c", f[b][i], i < MedN + 3 ? ' ' : '\n');
*/
   b ^= 1;
   for (i = 0; i <= MaxN; i++)
    f[b][i] = -MaxC;
   for (i = 0; i <= MaxN; i++)
    for (j = 0; j <= MaxN; j++)
    {
     v = i + j - MaxN;
     v += MedN;
     if (v < 0 || v > MaxN)
      continue;
     f[b][v] = max (f[b][v], (f[!b][i] + f[!b][j]) * 0.5);
    }
  }

  printf ("%.20lf\n", f[b][MedN]);
 }

 return 0;
}
