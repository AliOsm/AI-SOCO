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

constexpr int MAXN = 100005;
int n;
int a[MAXN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    scanf("%d", &n);
    map<int, int> m;
    for (int i = 0; i < n; ++i) {
        scanf("%d", a + i);
        m[a[i]]++;
    }

    bool odd = false;
    for (auto& p : m) {
        odd |= (p.second % 2) == 1;
    }

    printf("%s\n", odd ? "Conan" : "Agasa");

    return 0;
}
