#define MAXSTACKSIZE [1024 * 1024 * 128]
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <hash_map>
#include <hash_set>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iterator>
#include <limits>
using namespace std;
#define mems(arr, val) memset(arr, val, sizeof(arr))
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define all(A) (A).begin(), A.end()
#define mp(a, b) make_pair(a, b)
#define forit(it, A) for(auto it = A.begin(); it != A.end(); it++)
typedef long long LL;
typedef pair<int, int> pii;
//const LL INF = INT_MAX;
const int MAXN = 100000 + 100;
const LL MOD = 1000000007;
const double EPS = 1e-6;

vector<int> p(1001);

void build()
{
    for(int i = 0; i < p.size(); ++i)
    {
        p[i] = i;
    }
}

int get_parent(int v)
{
    if (p[v] == v) return v;
    return p[v] = get_parent(p[v]);
}

void unionsets(int a, int b)
{
    a = get_parent(a);
    b = get_parent(b);
    if (a == b) return;
    if (rand() & 1)
    {
        p[a] = b;
    }
    else
    {
        p[b] = a;
    }
}

vector<vector<pair<int, int>>> minost(vector<vector<pair<int, int>>> &G)
{
    set<pair<int, pair<int, int>>> S;
    for(int i = 0; i < G.size(); ++i)
    {
        for(int j = 0; j < G[i].size(); ++j)
        {
            S.insert(mp(G[i][j].second, mp(i, G[i][j].first)));
        }
    }

    vector<vector<pair<int, int>>> ans(G.size());
    int tmpans = 0;
    while(S.size() > 0)
    {
        auto cur = *(S.begin());
        S.erase(cur);
        if (get_parent(cur.second.first) == get_parent(cur.second.second)) continue;
        unionsets(cur.second.first, cur.second.second);
        tmpans += cur.first;
        ans[cur.second.first].push_back(mp(cur.second.second, cur.first));
        ans[cur.second.second].push_back(mp(cur.second.first, cur.first));
    }

    return ans;
}

int G[1001][1001];
int main()
{
#ifdef MY_SOL
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif
    int n,m,k,w;
    cin>>n>>m>>k>>w;
    build();
    mems(G, MOD);

    vector<vector<string>> A(k, vector<string>(n));


    forn(i, 0, k)
    {
        string str;
        forn(j, 0, n)
        {
            cin>>A[i][j];
        }
    }

    for(int i = 0; i < A.size(); ++i)
    {
        for(int j = i + 1; j < A.size(); ++j)
        {
            int delta = 0;
            for(int r = 0; r < n; ++r)
            {
                for(int c = 0; c < m; ++c)
                {
                    delta += A[i][r][c] != A[j][r][c];
                }
            }

            G[i][j] = G[j][i] = min(delta * w, n * m);
        }
    }

    vector<vector<pair<int, int>>> G1(k);

    for(int i = 0; i < k; ++i)
    {
        for(int j = i + 1; j < k; ++j)
        {
            G1[i].push_back(mp(j, G[i][j]));
            G1[j].push_back(mp(i, G[i][j]));
        }
    }

    auto ans = minost(G1);

    queue<int> Q;

    bool used[1001];
    mems(used, false);

    Q.push(0);
    vector<pair<int ,int>> prt;
    prt.push_back(mp(1, 0));
    used[0] = true;
    int answer = n * m;
    while(Q.size() > 0)
    {
        auto cur = Q.front();
        Q.pop();

        for(int i = 0; i < ans[cur].size(); ++i)
        {
            if (used[ans[cur][i].first]) continue;
            prt.push_back(mp(ans[cur][i].first + 1, ans[cur][i].second == n * m ? 0 : cur + 1));
            answer += ans[cur][i].second;
            if (!used[ans[cur][i].first])
            {
                used[ans[cur][i].first] = true;
                Q.push(ans[cur][i].first);
            }
        }
    }

    cout<<answer<<endl;
    forn(i, 0, prt.size())
    {
        cout<<prt[i].first<<" "<<prt[i].second<<endl;
    }

    return 0;
}
