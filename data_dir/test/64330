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
#define N 100005
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
int t, a, b;
int main() {
  cin>>t;
  for (int i = 1; i <= t; ++i) {
    scanf("%d%d", &a, &b);
    int ans=max(a+a, b);
    ans = min(ans, max(b+b, a));
    ans = min(ans, max(a+b, max(a, b)));
    cout<<ans*ans<<endl;
  }
  return 0;
}
