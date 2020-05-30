#include <bits/stdc++.h>
using namespace std;

#define fr(i,n) _back
#define pb	push_back
#define eb	emplace_back
#define mk	make_pair
#define fi	first
#define se	second
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
typedef tuple<int,int,int> ti;
typedef vector<ti> vti;
typedef vector<ii> vii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const int T = 103;
int v[T];
vti aux[T];
priority_queue<ti,vti,greater<ti>> pq;

int main() {
    ios_base::sync_with_stdio(false);
    int n,m; cin >> n >> m;

    for(int i = 1; i <= m; i++) {
        int s,d,c;
        cin >> s >> d >> c;
        aux[s].eb(d,c,i);
        v[d] = m+1;
    }

    bool ok = 1;

    for(int i = 1; i <= n; i++) {
        while(!aux[i].empty()) {
            pq.emplace(aux[i].back());
            aux[i].pop_back();
        }

        if(v[i]) continue;

        if(!pq.empty()) {
            int d,c,id;
            tie(d,c,id) = pq.top();
            pq.pop();
            if(d <= i) { ok = 0; break; }
            c--;
            v[i] = id;
            if(c) pq.emplace(d,c,id);
        }
    }

    if(pq.size()) ok = 0;
    if(!ok) cout << -1 << endl;
    else for(int i = 1; i <= n; i++) cout << v[i] << (i==n?"\n":" ");




    return 0;
}

