#include <bits/stdc++.h>

using namespace std;

const int N = 205;

char s[N];

bool lower(char c) {
  return 'a' <= c && c <= 'z';
}

int main() {
  int n;
  scanf("%d %s", &n, s);
  int ans = 0;
  for (int i = 0; i < n; i++) {
    if (!lower(s[i])) continue;
    int j = i;
    while (j + 1 < n && lower(s[j + 1])) j++;
    set<char> ada;
    for (int k = i; k <= j; k++) ada.insert(s[k]);
    ans = max(ans, (int) ada.size());
    //printf("%d %d\n", i, j);
    i = j;
  }
  cout << ans << endl;
  return 0;
}
