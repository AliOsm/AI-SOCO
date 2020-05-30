#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <bitset>
#include <complex>

using namespace std;

using ll = long long;
using ld = long double;
using pii = pair<int, int>;

int n, p;
char s[100005];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf(" %d %d", &n, &p);
    scanf(" %s", s);

    bool poss = false;
    for (int i = 0; i + p < n; ++i) {
        if (s[i] == '.' and s[i + p] == '.') {
            s[i] = '0';
            s[i + p] = '1';
            poss = true;
            break;
        } else if (s[i] == '.') {
            s[i] = '0' + (1 - (s[i + p] - '0'));
            poss = true;
            break;
        } else if (s[i + p] == '.') {
            s[i + p] = '0' + (1 - (s[i] - '0'));
            poss = true;
            break;
        } else if (s[i] != s[i + p]) {
            poss = true;
            break;
        }
    }

    if (poss) {
        for (int i = 0; i < n; ++i) {
            if (s[i] == '.')
                s[i] = '0';
        }
        printf("%s\n", s);
    } else {
        printf("No\n");
    }
    
    return 0;
}
