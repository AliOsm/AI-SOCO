#include <iostream>
#include <cstring>
#define MOD 1000000007

using namespace std;

void copy(long long a[4][4], long long b[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            b[i][j] = a[i][j];
        }
    }
}

void mat_mult(long long a[4][4], long long b[4][4], long long c[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            c[i][j] = 0LL;
            for (int k = 0; k < 4; ++k) {
                c[i][j] += a[i][k] * b[k][j];
                c[i][j] %= MOD;
            }
        }
    }
}

void mat_pow(long long a[4][4], long long n, long long res[4][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            res[i][j] = i == j;
        }
    }

    long long temp[4][4];
    while (n > 0) {
        if (n & 1) {
            mat_mult(a, res, temp);
            copy(temp, res);
        }
        mat_mult(a, a, temp);
        copy(temp, a);

        n >>= 1;
    }
}

int main() {
    long long mat[4][4] = {{0, 1, 1, 1}, {1, 0, 1, 1}, {1, 1, 0, 1}, {1, 1, 1, 0}};
    long long res[4][4];

    memset(res, 0, sizeof(res));

    int n;
    cin >> n;
    mat_pow(mat, n, res);

    cout << res[3][3] << '\n';
    return 0;
}
