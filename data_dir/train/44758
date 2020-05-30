#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <utility>
#include <functional>
#include <cassert>

using namespace std;

const int N = 2e5 + 5;

int a[N], n, m;

bool can(int d) {
  vector<int> caf[d];
  for (int i = 0; i < n; i++) {
    caf[i % d].push_back(a[i]);
  }
  long long got = 0;
  for (int i = 0; i < d; i++) {
    for (int j = 0; j < caf[i].size(); j++) {
      got += max(0, caf[i][j] - j);
    }
  }
  return got >= m;
}

int main() {
  scanf("%d %d", &n, &m);
  for (int i = 0; i < n; i++) scanf("%d", a + i);
  sort(a, a + n);
  reverse(a, a + n);
  int l = 1, r = n + 1;
  while (l < r) {
    int mid = (l + r) >> 1;
    if (can(mid)) {
      r = mid;
    } else {
      l = mid + 1;
    }
  }
  if (l > n) {
    puts("-1");
  } else {
    cout << l << endl;
  }

  return 0;
}
