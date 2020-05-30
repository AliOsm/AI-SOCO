#include <bits/stdc++.h> 
using namespace std;

int MOD = 1e9 + 7;

typedef long long ll;
typedef vector<ll> row;
typedef vector<row> Matrix;

Matrix mult(const Matrix &a, const Matrix &b) {
    Matrix res(a.size(), row(b[0].size(), 0));

    for (int i = 0; i < a.size(); ++i)
        for (int j = 0; j < b[0].size(); ++j)
            for (int k = 0; k < a[0].size(); ++k)
                res[i][j] = (res[i][j] + a[i][k] * b[k][j] % MOD) % MOD;

    return res;
}

Matrix ident(int size) {

    Matrix res(size, row(size, 0));
    for (int i = 0; i < size; ++i)
        res[i][i] = 1;

    return res;
}

Matrix pow(Matrix b, ll p) {
    Matrix res = ident(b.size());

    for (int i = 0; i < 64; ++i) {
        if (1 & (p >> i)) res = mult(res, b);
        b = mult(b, b);
    }
    return res;

}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    Matrix adj(4, row(4));
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            adj[i][j] = i != j;

    int n;
    cin >> n;

    cout << pow(adj, n)[0][0];

}
