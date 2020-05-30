#include<bits/stdc++.h>
using namespace std;
const int maxn = 100005;
int mark[maxn], vist[maxn], parent[maxn];
set<int>graph[maxn], rev[maxn];
set<int> s;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;
    int start = 1;
    for(int i = 1; i <= n; i++)
    {
        int p,c;
        cin >> p >> c;
        mark[i] = c;
        parent[i] = p;
        if(p != -1)
        {
            graph[p].insert(i);
            rev[i].insert(p);
        }
    }
    for(int i = 1; i <= n; i++)
    {
        int tt = parent[i];
        if(mark[i])
        {
            //cout << i  << "*****->"<< endl;
            bool flag = true;
            for(auto x: graph[i])
            {
                if(mark[x] == 0)
                {
                    flag = false;
                }
            }
            if(flag)
            {
                //cout << i  << "---------->"<< endl;
                s.insert(i);
                for(auto x: rev[i])
                {
                    graph[x].erase(i);
                }
            }
            graph[i].clear();
            rev[i].clear();
            if(parent[i] != -1)
            {
                for(auto x: graph[i])
                    graph[parent[i]].insert(x);
            }
        }
    }
    if(s.size() == 0)  cout <<"-1";
    else
    {
        for(auto x: s)
        {
            cout << x << " ";
        }
    }
    return 0;
}

