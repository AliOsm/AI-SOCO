#include<bits/stdc++.h>
#define y0 waserdtfyguygthretwhrtrr
using namespace std;
typedef long long ll;
const int N = 1e5 + 897;
void exgcd(ll a,ll & x,ll b, ll & y, ll & g)
{
    if (b) {
        exgcd(b,y,a%b,x,g);
        y -= a/b*x;
    } else {
        g = abs(a);
        x = a/g;
        y = 0;
        return;
    }
}
ll cl(ll a,ll b)
{
    return (a+b-1)/b;
}
ll fl(ll a,ll b)
{
    if (a < 0)
        return -cl(-a,b);
    return a/b;
}
ll la,ra,ta, lb,rb, tb, x0, y0, g, ans = -1;
void sol(ll lt,ll rt, ll base, ll bo)
{
    ll gl = fl(lt+g-1,g), gr = fl(rt,g);
    if (gl > gr)
        return;
    ans = max(ans, base + bo * gr * g);
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> la >> ra >> ta >> lb >> rb >> tb;
    exgcd(ta,x0,-tb,y0,g);
    ll lt = lb - ra, rt = rb - la;
    sol(max(lt,max(lb-la,rb-ra)), rt, rb-la, -1);
    sol(lt,min(rt,min(lb-la,rb-ra)), ra-lb, 1);
    sol(max(lt,lb-la), min(rt,rb-ra), ra-la, 0);
    sol(max(lt,rb-ra), min(rt,lb-la), rb-lb, 0);
    cout << ans + 1 << '\n';
}
