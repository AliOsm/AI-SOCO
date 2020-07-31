#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

using ll = long long;

constexpr int MAXN = 1003;
int n, m, q;
char grid[MAXN][MAXN];
int visit[MAXN][MAXN];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

int solve(int sx, int sy) {
    if (visit[sx][sy] >= 0) {
        return visit[sx][sy];
    }

    queue<pair<int, int> > q;
    vector<pair<int, int> > seen;
    visit[sx][sy] = 0;
    q.push({sx, sy});

    int ans = 0;
    while (!q.empty()) {
        auto pos = q.front();
        q.pop();
        int x = pos.first;
        int y = pos.second;
        seen.push_back({x, y});

        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (grid[nx][ny] == '*') {
                ++ans;
            } else if (visit[nx][ny] == -1) {
                q.push({nx, ny});
                visit[nx][ny] = 0;
            }
        }
    }

    for (auto pos : seen) {
        visit[pos.first][pos.second] = ans;
    }

    return ans;
}

int main() {
    scanf("%d %d %d", &n, &m, &q);
    for (int i = 0; i < n; ++i) {
        scanf("%s", grid[i]);
    }

    memset(visit, -1, sizeof(visit));
    int x, y;
    while (q-- > 0) {
        scanf("%d %d", &x, &y);
        --x;
        --y;

        printf("%d\n", solve(x, y));
    }

    return 0;
}
