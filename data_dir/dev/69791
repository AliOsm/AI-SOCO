#include <iostream>
#include <queue>
#include <utility>
#define MAX_N 505
using namespace std;

typedef pair<int, int> pii;

int N, M, K;
char board[MAX_N][MAX_N];
bool mask[MAX_N][MAX_N];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int main() {
    cin >> N >> M >> K;
    int x, y, wall = 0;

    for (int i = 0; i < N; ++i) {
        cin >> board[i];
        for (int j = 0; j < M; ++j) {
            if (board[i][j] == '.') {
                x = i;
                y = j;
            } else {
                wall++;
            }
            mask[i][j] = true;
        }
    }

    queue<pii> q;
    q.push(make_pair(x, y));
    int count = (N * M - wall) - K;

    while (count > 0 && !q.empty()) {
        pii cur = q.front();
        q.pop();
        int i = cur.first;
        int j = cur.second;

        if (i < 0 || i >= N || j < 0 || j >= M || !mask[i][j] || board[i][j] == '#') {
            continue;
        }

        mask[i][j] = false;
        count--;

        for (int d = 0; d < 4; ++d) {
            q.push(make_pair(i + dx[d], j + dy[d]));
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cout << (!mask[i][j] ? board[i][j] : (board[i][j] == '.' ? 'X' : '#'));
        }
        cout << '\n';
    }
    return 0;
}
