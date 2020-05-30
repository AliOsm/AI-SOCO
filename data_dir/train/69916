#include "assert.h"
#include <iostream>

typedef long long int LL;

using namespace std;

LL getNumberOfCardsInFullHouse(LL floors) {
  return 3 * floors * (floors + 1) / 2 - floors;
}

LL getMaxHeight(LL n) {
  LL l = 0;
  LL r = 10000000;
  assert(getNumberOfCardsInFullHouse(r) > 1e13);
  while (l + 1 < r) {
    LL m = (l + r) / 2;
    if (getNumberOfCardsInFullHouse(m) <= n) l = m;
    else r = m;
  }
  return l;
}
 
LL solve(LL n) {
  LL mx = getMaxHeight(n);
  while ((mx + n) % 3) mx--;
  return (mx + 3 - 1) / 3;
}
 
int main() {
  LL n; cin >> n;
  cout << solve(n); 
}