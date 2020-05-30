#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second
#define eb emplace_back

typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector< pair<ll,ll> > vii;
const int INF = 0x3f3f3f3f;

const int T = 2e5 + 10;
int n,m,k,s;

ll dollar[T];
ll ponds[T];

ll minDoll[T][2];
ll minPond[T][2];
vii gd;
vii gp;

bool cmp(const ii &a, const ii &b) {
    if(a.se != b.se) return a.se < b.se;
    return false;
}

bool can(int d, bool flag) {
    ll mini = 0;

    int dol = 0;
    int pod = 0;
    int pegos = 0;
    if(flag) cout << d << endl;

    while(pegos < k) {
        if(mini > s) return false;
        if(dol < gd.size() and pod < gp.size()) {
            if(gd[dol].se * minDoll[d][0] <= gp[pod].se * minPond[d][0]) {
                mini += gd[dol].se * minDoll[d][0];
                pegos++;
                if(flag) cout << gd[dol].fi << " " << minDoll[d][1] << endl;
                dol++;
            } else {
                mini += gp[pod].se * minPond[d][0];
                pegos++;
                if(flag) cout << gp[pod].fi << " " << minPond[d][1] << endl;
                pod++;
            }
        } else if(dol < gd.size()) {
            mini += gd[dol].se * minDoll[d][0];
            pegos++;
            if(flag) cout << gd[dol].fi << " " << minDoll[d][1] << endl;
            dol++;
        } else if(pod < gp.size()) {
            mini += gp[pod].se * minPond[d][0];
            pegos++;
            if(flag) cout << gp[pod].fi << " " << minPond[d][1] << endl;
            pod++;
        }
    }

    return (mini <= s);
}

void read() {
    cin >> n >> m >> k >> s;

    int type, price;
    
    for(int i = 1; i <= n; i++) cin >> dollar[i];
    for(int i = 1; i <= n; i++) cin >> ponds[i];
    for(int i = 1; i <= m; i++) { 
        cin >> type >> price;
        if(type == 1) gd.eb(i,price);
        else gp.eb(i,price);
    }
}

void pre() {
    sort(gd.begin(), gd.end(), cmp);
    sort(gp.begin(), gp.end(), cmp);

    minDoll[0][0] = INF;
    minDoll[0][1] = INF;
    minPond[0][0] = INF;
    minPond[0][1] = INF;

    for(int i = 1; i <= n; i++) {
        if(dollar[i] < minDoll[i-1][0]) {
            minDoll[i][0] = dollar[i];
            minDoll[i][1] = i;
        } else {
            minDoll[i][0] = minDoll[i-1][0];
            minDoll[i][1] = minDoll[i-1][1];
        }
        if(ponds[i] < minPond[i-1][0]) {
            minPond[i][0] = ponds[i];
            minPond[i][1] = i;
        } else {
            minPond[i][0] = minPond[i-1][0];
            minPond[i][1] = minPond[i-1][1];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    read(); 
    pre();

    int l = 1;
    int r = n;

    while(l <= r) {
        int mid = (l+r) >> 1;
        if(can(mid,0)) r = mid-1;
        else l = mid+1;
    }
   
    if(l <= n and can(l,0)) can(l,1);
    else cout << -1 << endl;
        
    return 0;
}

