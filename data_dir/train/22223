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

int ele(int x, int y) {
    int ans = 2;
    for(int i = 2; i <= y; i++)
        ans = ans*x;
    if(y == 0) return 1;
    return ans;
}

int main() {
    int tc;
    scanf("%d", &tc);
    int x;
    while(tc--) {
        scanf("%d", &x);
        printf("%d\n", ele(2,__builtin_popcount(x)));
    }
    return 0;
}

