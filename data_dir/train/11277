#include <iostream>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <utility>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;

int n;
vector<int> graph[10004];
bool visit[10004];

void dfs(int x) {
    visit[x] = true;
    for (int y : graph[x]) {
        if (!visit[y]) {
            dfs(y);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n;

    int x;
    for (int i = 1; i <= n; ++i) {
        cin >> x;
        graph[i].push_back(x);
        graph[x].push_back(i);
    }

    memset(visit, 0, sizeof(visit));

    int ans = 0;
    for (int i = 1; i <= n; ++i) {
        if (!visit[i]) {
            dfs(i);
            ++ans;
        }
    }

    cout << ans << '\n';

    return 0;
}
