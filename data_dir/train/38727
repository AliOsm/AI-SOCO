#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#define N 52
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
int t, n;
int s[N];
int main() {
  cin>>t;
  for (int i = 1; i <= t; ++i) {
    scanf("%d", &n);
    for (int i =1; i <= n; ++i) {
      scanf("%d", &s[i]);
    }
    int on = 0, en = 0;
    for (int i = 1; i <= n; ++i) {
      if (s[i] % 2) on++;
      else en++;
    }
    if ((on%2) && (en%2)) {
      sort(s+1, s+n+1);
      int i;
      for (i = 2; i <= n; ++i) {
        if (s[i]-s[i-1] == 1) break;
      }
      if (i <= n) {
        cout<<"YES"<<endl;
      } else {
        cout<<"NO"<<endl;
      }
    } else {
      cout<<"YES"<<endl;
    }
  }
  return 0;
}
