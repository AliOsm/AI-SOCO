#include "bits/stdc++.h"
using namespace std;

const int maxn = 1e5 + 10;

int n;
char s[maxn];

int solve() {
    int ans = 0;
    int last, x = 0, y = 0;
    if(s[0] == 'U') last = 1, ++y;
    else last = 0, ++x;

    for(int i = 1; i < n; ++i) {
	if(s[i] == 'U') ++y;
	else ++x;

	if(x != y) {
	    int Last = -1;
	    if(x > y) Last = 0;
	    else Last = 1;

	    if(Last != last) ++ans;
	    last = Last;
	}
    }
    return ans;
}

int main() {
    scanf("%d %s", &n, s);
    printf("%d\n", solve());
    return 0;
}
