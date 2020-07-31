#include <bits/stdc++.h>

using namespace std;

const int N = 105;

int a[N];

int main() {
  int n;
  scanf("%d", &n);
  for(int i = 1; i <= n; i++) {
    scanf("%d", a + i);
  }  
  for(int it = 1; it <= n; it++) {
    for(int i = 1; i < n; i++) {
      if(a[i] > a[i + 1]) {
        printf("%d %d\n", i, i + 1);
        swap(a[i], a[i + 1]);
      }
    }
  }
  return 0;
}
