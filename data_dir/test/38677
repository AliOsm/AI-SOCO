#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

using ll = long long;
using ld = long double;
using pii = pair<int, int>;
using vi = vector<int>;

int valid(int x, int y) {
    // no two of the girls fingers may touch
    if (y < x - 1) return false;

    // no three of the boys fingers may touch
    // 1234567890
    // 0011223344
    int gaps = (y - 1) / 2;
    if (x < gaps)
        return false;

    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int al, ar;
    int bl, br;
    cin >> al >> ar;
    cin >> bl >> br;
    if (valid(al, br) or valid(ar, bl)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    
    return 0;
}
