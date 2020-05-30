#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<int,int> ii;
typedef vector< pair<int,int> > vii;
const int INF = 0x3f3f3f3f;

struct query { int ind, l, r; };
const int T = 1e5 + 1000;
const int N = sqrt(T);
int v[T];
int ans[T];
vector<query> qrs;
int track[T];
int resp;

void add(int ind) {
    if(v[ind] > 1e5 + 10) return;
    track[v[ind]]++;
    if(v[ind] == track[v[ind]]) resp++;
    if(v[ind] + 1 == track[v[ind]]) resp--;
}

void tira(int ind) {
    if(v[ind] > 1e5 + 10) return;
    track[v[ind]]--;
    if(v[ind] == track[v[ind]]) resp++;
    if(v[ind] - 1 == track[v[ind]]) resp--;
}

void mo() {
    int l = 0;
    int r = 0;
    add(0);
    for(auto x : qrs) {
        while(r < x.r) add(++r);
        while(r > x.r) tira(r--);
        while(l < x.l) tira(l++);
        while(l > x.l) add(--l);
        ans[x.ind] = resp;
    }
}

bool cmp(const query &a, const query &b) {
    if(a.l / N != b.l / N) return a.l < b.l;
    return a.r > b.r;
}

int main() {
    ios::sync_with_stdio(false);
    int n, q;
    cin >> n >> q;
    for(int i = 0; i < n; i++) cin >> v[i];
    int a,b;
    for(int i = 0; i < q; i++) {
        cin >> a >> b;
        qrs.pb({i,a-1,b-1});
    }
    sort(qrs.begin(), qrs.end(), cmp);
    mo();
    for(int i = 0; i < q; i++) cout << ans[i] << endl;
    return 0;
}

