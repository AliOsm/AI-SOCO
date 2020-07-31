#include <iostream>
#define MAX 60
using namespace std;

long long choose[65][65];

void gen_comb() {
    for (int i = 0; i <= MAX; ++i) {
        choose[i][0] = 1;
        choose[i][i] = 1;
    }

    for (int i = 2; i <= MAX; ++i) {
        for (int j = 1; j < i; ++j) {
            choose[i][j] = choose[i - 1][j - 1] + choose[i - 1][j];
        }
    }
}

int main() {
    gen_comb();

    int n, m, t;
    cin >> n >> m >> t;
    // n choose 4
    // m choose 1
    long long ans = 0;
    for (int i = 4; i <= t; ++i) {
        int j = t - i;
        if (j < 1) continue;
        ans += choose[n][i] * choose[m][j];
    }

    cout << ans << '\n';
    return 0;
}
