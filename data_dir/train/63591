#include <cstdio>
#include <utility>
#include <cmath>
#include <queue>
#include <algorithm>
#define X first
#define Y second
#define D first
#define I second
using namespace std;
typedef pair<int,int> pii;
typedef pair<double,int> pdi;

void rc(pii& c)
{
    scanf("%d%d", &c.X, &c.Y);
}

double dist(const pii& a, const pii& b)
{
    double dx = a.X - b.X, dy = a.Y - b.Y;
    return sqrt(dx*dx+dy*dy);
}

int main()
{
    pii a, b, t;
    int n;
    double ans = 0.0;
    deque<pdi> pa, pb;
    rc(a); rc(b); rc(t);
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        pii bottle;
        rc(bottle);
        double dt = dist(bottle, t);
        ans += dt * 2.0;
        double da = dist(bottle, a), db = dist(bottle, b);
        pa.push_back({da - dt, i});
        sort(pa.begin(), pa.end());
        if (pa.size() > 2)
            pa.pop_back();

        pb.push_back({db - dt, i});
        sort(pb.begin(), pb.end());
        if (pb.size() > 2)
            pb.pop_back();
    }

    if (pa[0].I == pb[0].I) {
        if (pa[0].D + (pb[1].D < 0 ? pb[1].D : 0.0) < pb[0].D + (pa[1].D < 0 ? pa[1].D : 0.0))
            pb.pop_front();
        else
            pa.pop_front();
    }
    
    if (pa[0].D < 0 && pb[0].D < 0)
        ans += pa[0].D + pb[0].D;
    else
        ans += min(pa[0].D, pb[0].D);

    printf("%.16f\n", ans);
}
