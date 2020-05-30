#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    ll a, b, x, y;
    cin >> a >> b >> x >> y;

    int g = gcd(x, y);
    x /= g;
    y /= g;

    ll w = 0;
    ll h = 0;

    ll x1 = a - (a % x);
    ll y1 = (x1 / x) * y;
    // cout << "1: " << x1 << ' ' << y1 << '\n';
    if (x1 <= a and y1 <= b and x1 * y1 > w * h) {
        w = x1;
        h = y1;
    }

    ll y2 = b - (b % y);
    ll x2 = (y2 / y) * x;
    // cout << "2: " << x2 << ' ' << y2 << '\n';
    if (x2 <= a and y2 <= b and x2 * y2 > w * h) {
        w = x2;
        h = y2;
    }

    cout << w << ' ' << h << '\n';

    return 0;
}
