#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <bitset>
#include <functional>
#include <vector>

#define ll long long
using namespace std;

vector<int> edges[111111];

void dfs(int par,int u, vector<int>* verts) {
    verts->push_back(u);
    for(int v : edges[u]) {
        if (v == par)
            continue;
        dfs(u,v,verts);
    }
}


ll C[3][111111];
int ans[111111];

void Solve(int n) {
    int st = -1;
    for(int i=1;i<=n;i++) {
        if (edges[i].size() > 2) {
            cout << -1 << endl;
            return;
        }
        if (edges[i].size() == 1) {
            st = i;
        }
    }
    
    vector<int> verts;
    dfs(-1, st, &verts);
    
    vector<int> P;
    P.push_back(0);
    P.push_back(1);
    P.push_back(2);
    
    ll min_cost = (1ll<<61);
    do {
        ll curr_cost = 0;
        for(int j=0;j<verts.size();j++) {
            int c = P[j%3];
            curr_cost += C[c][verts[j]];
        }
        if (curr_cost < min_cost) {
            min_cost = curr_cost;
            for(int j=0;j<verts.size();j++) {
                ans[verts[j]]=P[j%3];
            }
        }
        
    }while(next_permutation(P.begin(),P.end()));
    
    cout << min_cost << endl;
    for(int i=1;i<=n;i++)
        printf("%d ",ans[i]+1);
    cout << endl;
}


int main() {
    int n;
    cin>>n;
    for(int j=0;j<3;j++) {
        for(int i=1;i<=n;i++) {
            cin>>C[j][i];
        }
    }
    for(int i=1;i<=n-1;i++) {
        int u,v;
        cin>>u>>v;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }
    Solve(n);
}
