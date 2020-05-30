#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define ull unsigned long long
#define all(v)    ((v).begin()),((v).end())
#define clr(a,b)  memset(a,b,sizeof(a))
void debug() {
#ifndef ONLINE_JUDGE
  freopen("input.in", "rt", stdin);
// freopen("output.txt", "wt", stdout);
#endif
  cout << fixed << setprecision(0);
  ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
}

int const N = 1e9 + 9, OO = 1e9;

int arr[4];

int main() {
  debug();
  for (int i = 0; i < 4; ++i) {
    cin >> arr[i];
  }
  sort(arr, arr + 4);
  int c = arr[1] + arr[2] - arr[3];
  cout << arr[1] - c << " " << arr[2] - c << " " << c;
  return 0;
}