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
const int T = 6e5 + 10;
int a, b;
int v[T];
int seg[4*T];
vector<int> vi;
map<int,int> id;

struct node {
    int i,l,r;

    node(int i, int l, int r) :
        i(i), l(l), r(r) {}
};

vector<node> ve;

void build(int node, int i, int j) {
    if(i == j) seg[node] = v[i];
    else {
        int mid = (i + j) >> 1;
        build(2*node, i, mid);
        build(2*node+1, mid+1, j);
        seg[node] = min(seg[2*node], seg[2*node+1]);
    }
}

int query(int node, int i, int j) {
    if(i > b or j < a) return INF;
    if(i >= a and j <= b) return seg[node];
    int mid = (i + j) >> 1;
    return min(query(2*node, i, mid), query(2*node+1, mid+1, j));
}


int main() {
    ios::sync_with_stdio(false);
    int q, l, r;
    cin >> q;

    for(int i = 1; i <= q; i++) {
        cin >> l >> r;
        ve.eb(i,l,r);
        vi.pb(l); vi.pb(l-1); vi.pb(r);
    }

    sort(vi.begin(), vi.end());
    vi.resize(unique(vi.begin(), vi.end()) - vi.begin());
    for(int i = 0; i < vi.size(); i++)
        id[vi[i]] = i+1;
        


    for(int i = 0; i < ve.size(); i++) {
        int l = id[ve[i].l]; int r = id[ve[i].r];
        v[l] += 1;
        if(r+1 < T) v[r+1] -= 1;
    }

    for(int i = 1; i < T; i++)
        v[i] += v[i-1];

    build(1,1,T-1);


    for(int i = 0; i < ve.size(); i++) { 
        a = id[ve[i].l]; b = id[ve[i].r];
        if(query(1,1,T-1) > 1) { cout << ve[i].i << endl; return 0; }
    }
    cout << -1 << endl;

    return 0;
}

