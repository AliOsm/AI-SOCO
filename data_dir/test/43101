#include <bits/stdc++.h>
using namespace std;

bool can[101];
int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifndef ONLINE_JUDGE
//  freopen("test.in", "rt", stdin);
#endif

    int n, m;
    cin >> n >> m;

    while (n--) {
        int x;
        cin >> x;
        while (x--) {
            int tmp;
            cin >> tmp;
            can[tmp - 1] = 1;
        }
    }

    string ans[] = { "NO" ,"YES"};
    cout << ans[*min_element(can, can + m)];
    return 0;

}
