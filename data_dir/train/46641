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
const int N = 1e5 + 5;
int n, m;
int first[N];
map<pair<int,int>, int> mp;


int main() {
    scanf("%d %d", &n, &m);
    for(int i = 0; i < n; i++) 
        scanf("%d", first + i);
    
    for(int i = 0; i < m-1; i++) {
        int at;
        scanf("%d", &at);
        for(int j = 0; j < n-1; j++) {
            int dps; scanf("%d", &dps);
            if(mp.count(ii(at,dps))) mp[ii(at,dps)]++;
            else mp[ii(at,dps)] = 1;
            at = dps;
        }
    }

    int i = 0;
    ll ans = 0;
    while(i < n) {
        int j = i;
        while(j + 1 < n and mp[ii(first[j],first[j+1])] == m-1)
            j++;
        ll len = (j-i+1);
        ans += (len * (len+1))>>1;
        i = j + 1;
    }

    printf("%lld\n", ans);
    return 0;
}

