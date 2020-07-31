#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
#define F first
#define S second
vector<array<pii,3>> p;
array<pii,3> cur;
void dfs(int i,int k,int x)
{
    if (i == 8) {
        if (k)
            return;
        int t[3],tp=0;
        for (int j=0;j<3;++j)
            if (j < x) {
                for (int w=0;w<cur[j].S;++w)
                    t[tp++] = cur[j].F;
            } else {
                cur[j] = {0,0};
            }
        bool ok;
        do {
            ok = 1;
            for (int j=0;j<3;++j)
                ok &= t[j]>>j&1;
        } while (!ok && next_permutation(t,t+3));
        if (ok)
            p.push_back(cur);
        return;
    }
    dfs(i+1,k,x);
    for (int w=1;w<=k;++w) {
        cur[x]={i,w};
        dfs(i+1,k-w,x+1);
    }
}
int g(int a,int b) {return b?g(b,a%b):a;}
ll h(ll n,ll k)
{
    if (n <= 0)
        return 0;
    n += k-1;
    switch(k){
        case 1:return n;
        case 2:return n*(n-1)/2;
        default: return n*(n-1)/2*(n-2)/3;
    }
}
const int N = 1e5+87;
int d[N];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    dfs(1,3,0);
    cerr << p.size() << endl;
    for (int i = 1; i*i < N; ++i) {
        d[i*i] += 1;
        for (int j = i*(i+1); j < N; j += i)
            d[j] += 2;
    }
    int t,a,b,c,s[8];
    cin >> t;
    while (t--) {
        cin >> a >> b >> c;
        int ab=g(a,b),ac=g(a,c),bc=g(b,c);
        int abc=g(ab,c);
        s[1|2|4] = d[abc];
        s[1|2] = d[ab] - d[abc];
        s[1|4] = d[ac] - d[abc];
        s[2|4] = d[bc] - d[abc];
        s[1] = d[a] - d[ab] - d[ac] + d[abc];
        s[2] = d[b] - d[ab] - d[bc] + d[abc];
        s[4] = d[c] - d[ac] - d[bc] + d[abc];
        ll ans = 0;
        for (const auto & e : p) {
            ll o = 1;
            for (int j = 0; j < 3; ++j)
                if (e[j].F)
                    o *= h(s[e[j].F],e[j].S);
            ans += o;
        }
        cout << ans << '\n';
    }
}
