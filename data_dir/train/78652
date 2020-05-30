#include <bits/stdc++.h>
using namespace std;
int n, p2n, arr[3003], mx, road[3003], ans[3003];
void bt(int i, int sum) {
    if (i * 2 >= p2n) {
        road[i] = sum;
        mx = max(mx, sum);
        return;
    }
    bt(2 * i, sum + arr[2 * i]);
    bt(2 * i + 1, sum + arr[2 * i + 1]);
}

int main() {
    cin >> n;
    p2n = round(pow(2, n + 1));
    for (int i = 2; i < p2n; ++i)
        cin >> arr[i];
    bt(1, 0);
    for (int i = p2n / 2; i < p2n; ++i)
        ans[i] = mx - road[i];
    for (int lvl = n - 1; lvl; --lvl) {
        int st = round(pow(2, lvl));
        for (int j = st; j < 2 * st; ++j) {
            int mn = min(ans[2 * j], ans[2 * j + 1]);
            ans[j] = mn;
            ans[2 * j] -= mn;
            ans[2 * j + 1] -= mn;
        }
    }
    int res = 0;
    for (int i = 0; i < 3003; ++i)
        res += ans[i];
    cout << res;
}
