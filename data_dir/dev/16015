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

const int T = 2e5 + 10;
int v[T];

int main() {
    ios::sync_with_stdio(false);
    int n; cin >> n;
    for(int i = 1; i < n; i++) cin >> v[i];
    set<int>track;
    set<int>ans;
    for(int i = 1; i < n; i++) {
        v[i] += v[i-1];
        track.insert(v[i]);
    }
    if(track.size() == n-1) {
        int ini;
        int maior;
        maior = *track.rbegin();
        if(maior == -1) ini = n;
        else ini = n-maior;
        v[0] = ini;
        ans.insert(ini);
        for(int i = 1; i < n; i++) ans.insert(ini + v[i]);
        if(*ans.begin() == 1 and *ans.rbegin() == n and ans.size() == n) {
            cout << v[0] << " ";
            for(int i = 1; i < n; i++) cout << ini + v[i] << " ";
            cout << endl;
        } else { cout << -1 << endl; return 0; }
    } else { cout << -1 << endl; return 0; } 

    return 0;
}

