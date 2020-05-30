#include<bits/stdc++.h>
using namespace std;
const int N = 1e5 + 7;
struct node
{
    bool f;
    int nxt[26];
} t[N];
int tp = 0;
typedef priority_queue<int> pq;
void ins(const string & s)
{
    int o = 0;
    for (int i = 0; i < s.size(); ++i) {
        int c = s[i] - 'a';
        int & p = t[o].nxt[c];
        if (!p)
            p = ++tp;
        o = p;
    }
    t[o].f = 1;
}
long long dfs(pq & p, int u = 0,int d = 0)
{
    pq q;
    long long s = 0;
    for (int i = 0; i < 26; ++i)
        if (t[u].nxt[i])
            s += dfs(q,t[u].nxt[i],d+1);
    if (u) {
        if (!t[u].f) {
            if (q.size()) {
                s -= q.top();
                q.pop();
                q.push(d);
                s += d;
            }
        } else {
            q.push(d);
            s += d;
        }
    }
    if (p.size() < q.size())
        p.swap(q);
    for (;q.size();p.push(q.top()),q.pop());
    return s;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        ins(s);
    }
    pq _p;
    cout << dfs(_p) << endl;
}
