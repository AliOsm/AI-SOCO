#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <queue>
#include <utility>
#include <map>

using namespace std;

int M, S;
char min_val[101];
char max_val[101];

void find_min(int M, int S) {
    if (S == 0) {
        min_val[0] = '0';
        return;
    }

    int sum = S;
    for (int i = 0; i < M; ++i) {
        int chars_left = M - i - 1;
        int sum_left = 9 * chars_left;

        if (sum <= sum_left) {
            char nextChar = (i == 0) ? '1' : '0';
            min_val[i] = nextChar;
            sum -= (nextChar - '0');
        } else {
            int diff = sum - sum_left;
            if (diff >= 10) {
                min_val[0] = '0';
                break;
            } else {
                min_val[i] = '0' + diff;
                sum -= diff;
            }
        }
    }
}

void find_max(int M, int S) {
    int sum = S;
    for (int i = 0; i < M; i++) {
        if (sum > 9) {
            max_val[i] = '9';
            sum -= 9;
        } else {
            max_val[i] = '0' + sum;
            sum = 0;
        }
    }
}

int main() {
    cin >> M >> S;
    if (M == 1) {
        if (S <= 9) {
            cout << S << " " << S << '\n';
        } else {
            cout << "-1 -1" << '\n';
        }
    } else {
        find_min(M, S);
        find_max(M, S);

        if (min_val[0] == '0' || max_val[0] == '0') {
            cout << "-1 -1";
        } else {
            for (int i = 0; i < M; i++) {
                cout << min_val[i];
            }
            cout << ' ';
            for (int i = 0; i < M; i++) {
                cout << max_val[i];
            }
        }
        cout << '\n';
    }

    return 0;
}
