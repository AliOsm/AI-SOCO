#include<bits/stdc++.h>

using namespace std;

typedef long long LL;
typedef unsigned long long uLL;
typedef long double ldb;
typedef pair<int,int> pii;

map<int, set<int>> se;


int parr[100000 + 1];

void add(int ind, int val)
{
    while(ind<=100000)
    {
        parr[ind] += val;
        ind = ind + (ind & -ind);
    }
}

int sum(int ind)
{
    int ans = 0;
    while(ind>0)
    {
        ans += parr[ind];
        ind = ind - (ind & -ind);
    }
    return ans;
}

int msum(int from, int to)
{
    ++from; ++to;
    if(to >= from)
        return sum(to) - sum(from-1);
    return sum(100001) - sum(from-1) + sum(to);
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int n, inp;
    vector<int> A;
    cin>>n;
    for(int i = 0; i < n; ++i)
    {
        cin>>inp;
        A.push_back(inp);
        se[inp].insert(i);
        add(i+1, 1);
    }
    vector<int> B = A;
    sort(B.begin(), B.end());
    int cur = 0;
    LL ans = 0;
    for(int mi: B)
    {
        auto x = se[mi].lower_bound(cur);
        if(x == se[mi].end())
            x = se[mi].begin();
        ans += msum(cur, *x);
        add(*x+1, -1);
        cur = *x + 1;
        se[mi].erase(x);
        if(cur >= n)
            cur = 0;
    }

    cout<<ans<<endl;

    return 0;
}
