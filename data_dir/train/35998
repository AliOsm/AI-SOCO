#include <bits/stdc++.h>
using namespace std;

void fn(long long &x, long long n) {
    if (x > n) x = n;
    if (x < 1) x = 1;
}

int main() {
    long long n, a;
    cin >> n >> a;
    long long arr[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i];
    long long sm = accumulate(arr, arr + n, 0LL);
    for (int i = 0; i < n; ++i) {
        long long lw = a - sm + arr[i], up = a - n + 1;
        fn(up, arr[i]), fn(lw, arr[i]);
        cout << arr[i] - up + lw - 1 << ' ';
    }
}
