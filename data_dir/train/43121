#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int n_ = 1e5 + 10;
int n, m, a[n_], b[n_];
int main() {
    scanf("%d %d", &n, &m);
    vector<ll> v;
    ll sum = 0;
    for(int i = 0; i < n; i++) {
        scanf("%d %d", a + i, b + i);
        sum += a[i];
        v.push_back(a[i] - b[i]);
    }
    sort(v.begin(), v.end());
    int cnt = 0;
    for(int i = n - 1; i >= 0; i--) {
        if(sum <= m) break;
        sum -= v[i];
        cnt++;
    }
    if(sum > m) {
        printf("-1\n");
    } else {
        printf("%d\n", cnt);
    }
}
