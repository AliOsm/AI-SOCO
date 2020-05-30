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
    int xp, noob;
    cin >> xp >> noob;
    int maxi = 0;

    for(int i = 0; 2*i <= xp and i <= noob; i++) {
        int restxp = xp - 2*i;
        int restnoob = noob - i;
        int j = restxp;
        if(restnoob/2 < j) j = restnoob/2;
        if(i + j > maxi) maxi = i + j;
    }
    cout << maxi << endl;
    return 0;
}

