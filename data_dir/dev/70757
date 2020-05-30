#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int N;
string S;
int a[100005];
int dp[100005][2][3];
// pos, last char, flip_state
// flip_State 0 = never flip, 1 = in flip, 2 = done flip
// if in_flip, last char is NOT the last char

int main() {
    cin >> N;
    cin >> S;

    memset(dp, 0, sizeof(dp));

    for (int i = 0; i < N; ++i) {
        a[i] = (S[i] == '1');
    }

    for (int j = 0; j <= 1; ++j) {
        for (int k = 0; k <= 2; ++k) {
            dp[0][j][k] = (k & 1) ^ (a[0] == j);
        }
    }

    for (int i = 1; i < N; ++i) {
        //00, 01, 10
        for (int j = 0; j <= 1; ++j) {
            for (int k = 0; k < 3; ++k) {
                dp[i][j][k] = dp[i - 1][j][k];
            }
        }

        for (int j = 0; j <= 1; ++j) {
            if (a[i] == j) {
                dp[i][j][0] = max(dp[i][j][0], 1 + dp[i - 1][1 - j][0]);
            }
        }

        for (int j = 0; j <= 1; ++j) {
            dp[i][j][1] = max(dp[i][j][1], dp[i][1 - j][0]);
            if (a[i] != j) {
                dp[i][j][1] = max(dp[i][j][1], max(1 + dp[i - 1][1 - j][0], 1 + dp[i - 1][1 - j][1]));
            }
        }

        for (int j = 0; j <= 1; ++j) {
            dp[i][j][2] = max(dp[i][j][2], dp[i][1 - j][1]);
            if (a[i] == j) {
                dp[i][j][2] = max(dp[i][j][2], max(1 + dp[i - 1][1 - j][1], 1 + dp[i - 1][1 - j][2]));
            }
        }
    }

    /*
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 2; ++j) {
            cout << dp[i][j][0] << ' ';
        }
        cout << '\n';
    }

    cout << '\n';

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 2; ++j) {
            cout << dp[i][j][1] << ' ';
        }
        cout << '\n';
    }

    cout << '\n';

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < 2; ++j) {
            cout << dp[i][j][2] << ' ';
        }
        cout << '\n';
    }
    */

    int ans = min(N, 2);
    for (int j = 0; j <= 1; ++j) {
        for (int k = 0; k <= 2; ++k) {
            ans = max(ans, dp[N - 1][j][k]);
        }
    }

    cout << ans << '\n';

    return 0;
}
