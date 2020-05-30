#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <utility>

using namespace std;

int main() {
    int N;
    cin >> N;
    int x;
    int a[200005];
    for (int i = 1; i <= N; ++i) {
        cin >> x;
        a[x] = i;
    }

    long long ans = 0;
    for (int i = 2; i <= N; ++i) {
        ans += abs(a[i] - a[i - 1]);
    }

    cout << ans << '\n';

    return 0;
}
