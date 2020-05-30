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

int main() {
    ios::sync_with_stdio(false);
    int n, chest, bic, back;
    chest = bic = back = 0;
    int aux1, aux2, aux3;
    cin >> n;
    for(int i = 1; i <= n; i += 3) {
        aux1 = aux2 = aux3 = 0;
        cin >> aux1;
        if(i + 1 <= n) cin >> aux2;
        if(i + 2 <= n) cin >> aux3;
        chest += aux1;
        bic += aux2;
        back += aux3;
    }
    if(chest > bic and chest > back) cout << "chest" << endl;
    else if(back > bic and back > chest) cout << "back" << endl;
    else cout << "biceps" << endl;

        

    return 0;
}

