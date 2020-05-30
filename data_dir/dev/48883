#pragma comment(linker, "/stack:252457298")
#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
mt19937 rng32(chrono::steady_clock::now().time_since_epoch().count());
mt19937_64 rng64(chrono::steady_clock::now().time_since_epoch().count());

int n, m, p; vector<int> s, cnt;
vector<vector<char>> A;
vector<vector<pair<int, int>>> InitialCoor;
int dx[] = {-1, +0, +0, +1};
int dy[] = {+0, -1, +1, +0};
queue<tuple<int, int, int>> Q;
vector<vector<bool>> vis;

void Input() {
	cin >> n >> m >> p; A.resize(n, vector<char>(m)); InitialCoor.resize(p);
    s.resize(p); cnt.resize(p, 0); vis.resize(n, vector<bool>(m, false));
    for (auto &z: s) cin >> z;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> A[i][j];
            if (A[i][j] >= '1' && A[i][j] <= '9') {
                InitialCoor[A[i][j]-'1'].push_back({i, j});
            }
        }
    }
}

void Solve() {
    for (int i=0; i<p; i++) {
        for (auto Point: InitialCoor[i]) {
            int x = Point.first, y = Point.second;
            vis[x][y] = true; Q.push({i, x, y});
        }
    }
    while (!Q.empty()) {
        tuple<int, int, int> T = Q.front();
        int id = get<0>(T);
        queue<tuple<int, int, int>> TmpQueue;
        while (!Q.empty() && get<0>(Q.front()) == id) {
            T = Q.front();
            int firstx = get<1>(T), firsty = get<2>(T);
            TmpQueue.push({s[id], firstx, firsty}); Q.pop();
        }
        while (!TmpQueue.empty()) {
            tuple<int, int, int> xT = TmpQueue.front(); TmpQueue.pop();
            int step = get<0>(xT), x = get<1>(xT), y = get<2>(xT);
            if (step == 0) continue;
            for (int dir=0; dir<4; dir++) {
                if (x + dx[dir] < 0 || x + dx[dir] >= n) continue;
                if (y + dy[dir] < 0 || y + dy[dir] >= m) continue;
                if (vis[x+dx[dir]][y+dy[dir]]) continue;
                if (A[x+dx[dir]][y+dy[dir]] != '.') continue;
                vis[x+dx[dir]][y+dy[dir]] = true;
                A[x+dx[dir]][y+dy[dir]] = char(49+id);
                TmpQueue.push({step-1, x+dx[dir], y+dy[dir]});
                Q.push({id, x+dx[dir], y+dy[dir]});
            }
        }
    }
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (A[i][j] < '1' || A[i][j] > '9') continue;
            cnt[A[i][j]-'1'] += 1;
        }
    }
    for (auto x: cnt) cout << x << " "; cout << endl;
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0);
	Input(); Solve(); return 0;
}

/**********************************************\
*  Ngoc-Mai Ngo, #Team4T's Deputy Leader     *
*  #Team4T Secondary Flagship - Destruction  *
\**********************************************/