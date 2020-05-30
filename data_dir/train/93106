#ifdef __APPLE__
#include "bits:stdc++.h"
#else
#include <bits/stdc++.h>
#endif

using namespace std;
typedef long long LL;
typedef pair<LL, LL> PLL;
auto scan = []{ static LL a; scanf("%lld", &a); return a;};


int main() {
  LL x1 = scan(), y1 = scan(), x2 = scan(), y2 = scan();
  if (x1 == x2 || y1 == y2) {
    printf("%lld\n", 4ll + 2 * (abs(y1 - y2) + abs(x1 - x2) + 1));
  }
  else {
    printf("%lld\n", 2ll * (1ll + abs(y1 - y2) + (1ll + abs(x1 - x2))));
  }
}
