#include <bits/stdc++.h>

using namespace std;

typedef long long Long;

struct Point {
    Long x, y;

    Long getDist(const Point &other) const {
        Long dx = x - other.x;
        Long dy = y - other.y;
        return dx * dx + dy * dy;
    }

    Point getSlope(const Point &other) const {
        Point res;
        res.x = x - other.x;
        res.y = y - other.y;
        Long g = __gcd(res.x, res.y);
        res.x /= g;
        res.y /= g;
        return res;
    }

    bool operator==(const Point& other) const {
        return x == other.x && y == other.y;
    }

} a, b, c;

int main() {
#ifdef Local
    freopen("test.in", "r", stdin);
#endif


    ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

    cin >> a.x >> a.y >> b.x >> b.y >> c.x >> c.y;

    Long ab = a.getDist(b);
    Long bc = b.getDist(c);

    Point m_ab = a.getSlope(b);
    Point m_bc = b.getSlope(c);

    if (ab != bc || (m_ab == m_bc)) {
        cout << "No";
    } else {
        cout << "Yes";
    }



    return 0;
}