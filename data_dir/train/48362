#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <cmath>
#include <set>
#include <map>
#define N 100005
using namespace std;
typedef long long ll;
const ll mod = 1000000007LL;
int n;
int a[N];
int main() {
  cin>>n;
  for (int i = 1; i <= n; ++i) {
    scanf("%d", &a[i]);
  }
  int id=-1;
  sort(a+1, a+n+1);
  int i;
  for (i = 2; i <= n; ++i) {
    if (a[i] == a[i-1]) {
      if (id<0) id = i;
      else break;
    }
  }
  if (i<=n) {
    cout<<"cslnb"<<endl;
  } else {
    if (id>=0) {
      if (a[id] == 0) {
        cout<<"cslnb"<<endl;
        return 0;
      }
      a[id]--;
      sort(a+1, a+n+1);
      for (int i = 2; i <= n; ++i) {
        if (a[i] == a[i-1]) {
          cout<<"cslnb"<<endl;
          return 0;
        }
      }
    }
    ll tot=0LL;
    for (int i = 0; i < n; ++i) {
      tot += a[i+1]-i;
    }
    if (tot&1) {
      if (id<0) cout<<"sjfnb"<<endl;
      else cout<<"cslnb"<<endl;
    } else {
      if (id<0) cout<<"cslnb"<<endl;
      else cout<<"sjfnb"<<endl;
    }
  }
  return 0;
}
