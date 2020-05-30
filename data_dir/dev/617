#include<bits/stdc++.h>
using namespace std;
const int inf = 1000000001;
const int MOD = 1000000007;
typedef long long Int;
#define FOR(i,a,b) for(int i=(a); i<=(b);++i)
#define mp make_pair
#define pb push_back
#define sz(s) (int)((s).size())

const int N = 200009;
Int ans[N+1];

int main() {
    //freopen("input.txt", "r", stdin);//freopen("output.txt", "w", stdout);
    int n,b;scanf("%d %d\n",&n, &b);
    set<pair<int,pair<int,int> > > q;
    Int s = 0;
    memset(ans, -1, sizeof(ans));

    FOR(i,1,n+1) {
        int t, d;
        if(i!=n+1) scanf("%d %d",&t, &d);
        while(!q.empty()) {
            int curt = q.begin()->first;
            int curd = q.begin()->second.first;
            int id = q.begin()->second.second;
            if(i!=n+1 && max(s, (Int)curt) > t) break;
            Int res = max(s, (Int)curt) + curd;
            ans[id] = res;
            s = res;
            q.erase(q.begin());
        }

        if(i!=n+1 && sz(q) < b) q.insert(mp(t, mp(d, i)));
    }

    FOR(i,1,n) cout<<ans[i]<<" "; cout<<endl;
}
